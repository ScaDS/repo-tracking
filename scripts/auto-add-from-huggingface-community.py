import os
import sys
from datetime import datetime

import requests
import yaml

from _github_utilities import create_branch, get_file_in_repository, write_file, send_pull_request
from generate_link_lists import load_dataframe


HUGGINGFACE_BASE_URL = "https://huggingface.co"
HUGGINGFACE_API_BASE_URL = "https://huggingface.co/api"


def main():
    """
    Import public resources from a Hugging Face organization into resources/scadsai.yml.

    Usage
    -----
    python scripts/auto-add-from-huggingface-community.py <repository> [organization]

    Examples
    --------
    python scripts/auto-add-from-huggingface-community.py scads/repo-tracking ScaDSAI
    """
    repository = sys.argv[1]
    organization = sys.argv[2] if len(sys.argv) > 2 else "ScaDSAI"
    yml_filename = "resources/scadsai.yml"

    df = load_dataframe("resources/")
    all_urls = str(df["url"].tolist())
    new_data = []
    log = [
        f"# {organization}",
        f"{HUGGINGFACE_BASE_URL}/{organization}",
    ]

    for resource in fetch_huggingface_resources(organization):
        data = complete_huggingface_data(resource)
        urls = data["url"] if isinstance(data["url"], list) else [data["url"]]

        if any(url in all_urls for url in urls):
            continue

        data["submission_date"] = datetime.now().isoformat()
        new_data.append(data)
        log.append(f"* [{data['name']}]({data['url']})")
        all_urls += "\n" + "\n".join(urls)

    if len(new_data) == 0:
        print("No new Hugging Face resources to add. Exiting.")
        return

    print(new_data)

    branch = create_branch(repository)
    print("New branch:", branch)

    huggingface_yml = yaml.dump(new_data, sort_keys=False, allow_unicode=True)
    file_content = get_file_in_repository(repository, branch, yml_filename).decoded_content.decode()
    print("yml file content length:", len(file_content))

    file_content += huggingface_yml
    write_file(
        repository,
        branch,
        yml_filename,
        file_content,
        f"Add Hugging Face entries from {organization}",
    )

    res = send_pull_request(
        repository,
        branch,
        f"Add Hugging Face content from {organization}",
        "Added contents:\n" + "\n".join(log),
    )

    print("Done.", res)


def fetch_huggingface_resources(organization):
    """
    Fetch models, datasets, and spaces owned by a Hugging Face organization.
    """
    resources = []
    resource_types = [
        ("models", "Model", ""),
        ("datasets", "Dataset", "datasets/"),
        ("spaces", "Hugging Face Space", "spaces/"),
    ]

    for api_path, resource_type, web_path in resource_types:
        for item in fetch_paginated(f"{HUGGINGFACE_API_BASE_URL}/{api_path}", {"author": organization, "full": "true"}):
            item["resource_type"] = resource_type
            item["api_path"] = api_path
            item["web_path"] = web_path
            resources.append(item)

    return resources


def fetch_paginated(url, params):
    """
    Fetch all pages from a Hugging Face list endpoint.
    """
    headers = get_headers()
    next_url = url
    next_params = dict(params)
    next_params["limit"] = 100

    while next_url is not None:
        response = requests.get(next_url, params=next_params, headers=headers, timeout=30)
        response.raise_for_status()

        data = response.json()
        if not isinstance(data, list):
            return

        for item in data:
            yield item

        next_url = get_next_link(response.headers.get("Link"))
        next_params = None


def get_next_link(link_header):
    """
    Extract the next page URL from an RFC 5988 Link header.
    """
    if not link_header:
        return None

    for link in link_header.split(","):
        parts = [part.strip() for part in link.split(";")]
        if len(parts) < 2 or parts[1] != 'rel="next"':
            continue
        return parts[0].strip("<>")

    return None


def complete_huggingface_data(resource):
    """
    Convert a Hugging Face API resource into the repository YAML schema.
    """
    repo_id = resource.get("modelId") or resource.get("id")
    card_data = resource.get("cardData") or {}
    if not isinstance(card_data, dict):
        card_data = {}
    tags = collect_tags(resource, card_data)
    web_path = resource.get("web_path", "")

    entry = {
        "authors": collect_authors(resource, card_data),
        "description": collect_description(resource, card_data),
        "name": repo_id.split("/")[-1],
        "publication_date": collect_publication_date(resource),
        "tags": tags,
        "type": resource["resource_type"],
        "url": f"{HUGGINGFACE_BASE_URL}/{web_path}{repo_id}",
    }

    license_name = collect_license(resource, card_data)
    if license_name:
        entry["license"] = license_name

    downloads = resource.get("downloads")
    if downloads is not None:
        entry["num_downloads"] = downloads

    return entry


def collect_authors(resource, card_data):
    """
    Prefer people who committed to the Hugging Face repository.
    """
    commit_authors = fetch_commit_authors(resource)
    if len(commit_authors) > 0:
        return commit_authors

    authors = card_data.get("authors") or card_data.get("author")
    if isinstance(authors, str):
        return [authors]
    if isinstance(authors, list) and len(authors) > 0:
        return authors

    return []


def fetch_commit_authors(resource):
    """
    Return unique commit author names or usernames from a Hugging Face repository.
    """
    repo_id = resource.get("modelId") or resource.get("id")
    api_path = resource.get("api_path")
    if not repo_id or not api_path:
        return []

    url = f"{HUGGINGFACE_API_BASE_URL}/{api_path}/{repo_id}/commits/main"
    authors = []
    seen_authors = set()

    try:
        commits = fetch_paginated(url, {})
        for commit in commits:
            for author in extract_commit_authors(commit):
                normalized_author = author.strip()
                author_key = normalized_author.lower()
                if normalized_author and author_key not in seen_authors:
                    authors.append(normalized_author)
                    seen_authors.add(author_key)
    except requests.RequestException as error:
        print(f"Could not retrieve Hugging Face commit authors for {repo_id}: {error}")

    return authors


def extract_commit_authors(commit):
    """
    Extract author names from Hugging Face commit metadata.
    """
    authors = commit.get("authors")
    if isinstance(authors, list):
        for author in authors:
            if isinstance(author, dict):
                name = author.get("fullname") or author.get("name") or author.get("user") or author.get("username")
                if name:
                    yield name
            elif isinstance(author, str):
                yield author

    author = commit.get("author")
    if isinstance(author, dict):
        name = author.get("fullname") or author.get("name") or author.get("user") or author.get("username")
        if name:
            yield name
    elif isinstance(author, str):
        yield author


def collect_description(resource, card_data):
    """
    Build a concise description from available Hugging Face metadata.
    """
    description = (
        resource.get("description")
        or card_data.get("description")
        or card_data.get("model_description")
        or card_data.get("dataset_info")
        or ""
    )

    if isinstance(description, dict):
        return yaml.dump(description, sort_keys=False, allow_unicode=True)

    return str(description)


def collect_publication_date(resource):
    """
    Use the creation date when available and fall back to last modification date.
    """
    publication_date = resource.get("createdAt") or resource.get("lastModified")
    if publication_date:
        return publication_date.split("T")[0]
    return datetime.now().date().isoformat()


def collect_tags(resource, card_data):
    """
    Combine API tags with common card metadata fields.
    """
    tags = []
    tags.extend(resource.get("tags") or [])

    pipeline_tag = resource.get("pipeline_tag") or card_data.get("pipeline_tag")
    if pipeline_tag:
        tags.append(pipeline_tag)

    for key in ["task_categories", "language", "pretty_name"]:
        value = card_data.get(key)
        if isinstance(value, list):
            tags.extend(value)
        elif isinstance(value, str):
            tags.append(value)

    tags.append("Hugging Face")
    return sorted({str(tag).replace("license:", "").strip() for tag in tags if str(tag).strip()})


def collect_license(resource, card_data):
    """
    Extract license information from card metadata or license tags.
    """
    license_name = card_data.get("license")
    if license_name:
        return license_name

    for tag in resource.get("tags") or []:
        if tag.startswith("license:"):
            return tag.replace("license:", "", 1)

    return None


def get_headers():
    """
    Return optional Hugging Face authentication headers.
    """
    token = os.getenv("HF_API_KEY") or os.getenv("HUGGINGFACE_API_KEY")
    if token:
        return {"Authorization": f"Bearer {token}"}
    return {}


if __name__ == "__main__":
    main()
