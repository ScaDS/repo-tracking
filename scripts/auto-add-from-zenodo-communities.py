# This script is executed when a new issue is created on our github repository. 
# In case the issue text consists only of a single line starting like a zenodo link, 
# it will retrieve all important details from the zenodo record, add it to a yml file
# and send a pull-request
import sys
from _github_utilities import create_branch, get_file_in_repository, get_issue_body, write_file, send_pull_request
import yaml
import os
import requests
import shutil
import pandas as pd
from generate_link_lists import (load_dataframe, update_yaml_file, complete_zenodo_data,
                                  all_content, find_parent_entry, merge_zenodo_entry)
from datetime import datetime

def main():
    """
    Main function to handle the process of retrieving Zenodo data and appending
    it to a YAML file in a GitHub repository.

    This function takes command-line arguments for the repository name and issue number,
    retrieves the issue body, checks if it's a valid Zenodo link, retrieves corresponding
    data, and appends it to a specified YAML file by creating a new branch and submitting
    a pull request.

    When a new record belongs to the same Zenodo concept as an existing entry
    (i.e. it is a new version of something already tracked), the existing entry
    is updated in-place rather than creating a duplicate.

    Returns
    -------
    None
    """
    repository = sys.argv[1]

    token = os.getenv('ZENODO_API_KEY')
    communities = ['scads-ai']

    yml_filename = "resources/scadsai.yml"

    # read "database"
    branch = create_branch(repository)
    print("New branch:", branch)
    log = []

    # Load existing resources for duplicate / parent detection
    existing_resources = all_content("resources/")['resources']
    all_urls_set = set()
    for r in existing_resources:
        urls = r.get('url', [])
        if isinstance(urls, str):
            urls = [urls]
        all_urls_set.update(urls)

    # Read and parse the target YAML file from the new branch
    file_content_str = get_file_in_repository(repository, branch, yml_filename).decoded_content.decode()
    print("yml file content length:", len(file_content_str))
    file_data = yaml.safe_load(file_content_str)
    if file_data is None:
        file_data = {'resources': []}

    for community in communities:
        log.append(f"# {community}")
        log.append(f"https://zenodo.org/communities/{community}")
        # new data
        response = requests.get('https://zenodo.org/api/records',
                                params={'communities': community,
                                        'access_token': token})
        try:
            online_data = response.json()
            hits = online_data["hits"]["hits"]
            urls = [u["links"]["self_html"] for u in hits]
        except requests.exceptions.JSONDecodeError:
            print(f"Error decoding JSON for community: {community}")
            continue

        for url in urls:
            print(url)
            data = complete_zenodo_data(url)

            if isinstance(data["url"], str):
                data["url"] = [data["url"]]

            # Skip if any of the record's URLs are already tracked
            if any(u in all_urls_set for u in data["url"]):
                continue

            conceptrecid = data.get('conceptrecid')

            # Check whether this is a new version of an already-tracked record
            parent = find_parent_entry(file_data['resources'], conceptrecid)

            if parent is not None:
                # Merge new-version metadata into the existing entry
                merge_zenodo_entry(parent, data)
                name = data.get("name", url)
                log.append(f"* Updated existing entry (new version): [{name}]({url})")
                print(f"  -> merged as new version of existing entry '{parent.get('name')}'")
            else:
                # Check all resources (other yml files) to avoid cross-file duplicates
                parent_other = find_parent_entry(existing_resources, conceptrecid)
                if parent_other is not None:
                    name = data.get("name", url)
                    log.append(f"* Skipped (parent entry found in another file): [{name}]({url})")
                    print(f"  -> parent found in a different file, skipping duplicate")
                else:
                    # Genuinely new entry
                    data['submission_date'] = datetime.now().isoformat()
                    name = data.get("name", url)
                    log.append(f"* [{name}]({url})")
                    file_data['resources'].append(data)
                    existing_resources.append(data)

            # Mark all URLs for this record as known
            for u in data["url"]:
                all_urls_set.add(u)

    # Save updated data back to the repository
    new_file_content = yaml.dump(file_data, allow_unicode=True)
    write_file(repository, branch, yml_filename, new_file_content,
               "Add/update entries from " + ", ".join(communities))

    log = "\n".join(log)
    res = send_pull_request(repository, branch,
                            "Add content from communities: " + ", ".join(communities),
                            f"Added/updated contents:\n{log}")

    print("Done.", res)



if __name__ == "__main__":
    main()
