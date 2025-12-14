"""
This script scans GitHub organizations listed in github_organizations.yml
for repositories with at least one star that are not yet listed in scadsai.yml.
Only repositories with commits within the last year are added, and forks are excluded.
It creates a pull request with newly discovered repositories.
"""
import sys
import os
import yaml
import requests
from datetime import datetime, timedelta, timezone
from _github_utilities import create_branch, get_file_in_repository, write_file, send_pull_request, get_github_repository
from generate_link_lists import load_dataframe


def load_organizations(file_path='resources/github_organizations.yml'):
    """
    Load the list of GitHub organizations from the YAML file.
    
    Parameters
    ----------
    file_path : str
        Path to the github_organizations.yml file.
    
    Returns
    -------
    list of str
        List of organization URLs.
    """
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    
    organizations = []
    for org_entry in data.get('organizations', []):
        url = org_entry.get('url', '')
        if url:
            # Extract organization name from URL
            org_name = url.replace('https://github.com/', '').strip('/')
            organizations.append(org_name)
    
    return organizations


def get_organization_repos(org_name):
    """
    Retrieve all repositories from a GitHub organization that have at least one star,
    are not forks, and had activity within the last year, using the REST endpoint
    https://api.github.com/orgs/{ORG}/repos.

    Parameters
    ----------
    org_name : str
        Name of the GitHub organization.

    Returns
    -------
    list of dict
        List of repository information dictionaries.
    """
    print(f"-> Scanning organization: {org_name}")

    access_token = os.getenv('GITHUB_API_KEY')
    headers = {
        'Accept': 'application/vnd.github+json'
    }
    if access_token:
        headers['Authorization'] = f"Bearer {access_token}"

    # Use timezone-aware UTC datetimes to avoid naive/aware comparison issues
    one_year_ago = datetime.now(timezone.utc) - timedelta(days=365)
    repos = []

    # Paginate through repos
    page = 1
    per_page = 100
    while True:
        url = f"https://api.github.com/orgs/{org_name}/repos"
        params = {
            'type': 'public',
            'per_page': per_page,
            'page': page,
            'sort': 'pushed'
        }
        try:
            resp = requests.get(url, headers=headers, params=params, timeout=30)
            if resp.status_code == 404:
                print(f"  Organization not found or inaccessible: {org_name}")
                break
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            print(f"Error accessing {url}: {e}")
            break

        if not data:
            break

        for r in data:
            try:
                # Basic filters: non-fork, stars >= 1
                if r.get('fork'):
                    print(f"  Skipped (fork): {r.get('full_name')}")
                    continue
                stars = int(r.get('stargazers_count') or 0)
                if stars < 1:
                    continue

                # Recent activity check via pushed_at
                pushed_at = r.get('pushed_at')
                last_push_dt = None
                if pushed_at:
                    # pushed_at is ISO 8601 string; ensure timezone-aware (UTC)
                    last_push_dt = datetime.fromisoformat(pushed_at.replace('Z', '+00:00'))
                    if last_push_dt.tzinfo is None:
                        last_push_dt = last_push_dt.replace(tzinfo=timezone.utc)
                if not last_push_dt or last_push_dt < one_year_ago:
                    print(f"  Skipped (no recent commits): {r.get('full_name')}")
                    continue

                repo_info = {
                    'name': r.get('name') or '',
                    'full_name': r.get('full_name') or '',
                    'url': r.get('html_url') or '',
                    'stars': stars,
                    'description': r.get('description') or '',
                    'created_at': (r.get('created_at') or '')[:10] if r.get('created_at') else None,
                    'last_push': last_push_dt.strftime('%Y-%m-%d') if last_push_dt else None,
                }
                repos.append(repo_info)
                print(f"  Found: {repo_info['full_name']} ({stars} stars, last push: {repo_info['last_push']})")
            except Exception as e:
                print(f"  Error processing repo entry: {e}")

        page += 1

    return repos


def get_repo_metadata(repo_url):
    """
    Retrieve detailed metadata for a GitHub repository.
    
    Parameters
    ----------
    repo_url : str
        URL of the GitHub repository.
    
    Returns
    -------
    dict
        Repository metadata formatted for scadsai.yml.
    """
    print(f"-> Getting metadata for: {repo_url}")
    
    # Extract owner/repo from URL
    parts = repo_url.replace('https://github.com/', '').strip('/').split('/')
    if len(parts) < 2:
        return None
    
    repo_name = f"{parts[0]}/{parts[1]}"
    
    try:
        repo = get_github_repository(repo_name)
        
        # Get contributors
        contributors = []
        try:
            for contributor in repo.get_contributors():
                # Try to get full name, fall back to login
                name = contributor.name if contributor.name else contributor.login
                contributors.append(name)
                if len(contributors) >= 10:  # Limit to first 10 contributors
                    break
        except Exception as e:
            print(f"  Warning: Could not fetch contributors: {e}")
        
        # Get topics/tags
        topics = list(repo.get_topics())
        
        # Get license
        license_name = None
        try:
            if repo.license:
                license_name = repo.license.spdx_id if repo.license.spdx_id else repo.license.name
        except Exception:
            pass
        
        metadata = {
            'name': repo.name,
            'description': repo.description or '',
            'authors': contributors if contributors else [repo.owner.login],
            'url': [repo_url],
            'tags': topics if topics else None,
            'license': license_name,
            'publication_date': repo.created_at.strftime('%Y-%m-%d') if repo.created_at else None,
            'submission_date': datetime.now().isoformat(),
            'type': 'software'
        }
        
        # Remove None values
        metadata = {k: v for k, v in metadata.items() if v is not None}
        
        return metadata
        
    except Exception as e:
        print(f"  Error getting metadata: {e}")
        return None


def is_repo_in_database(repo_url, existing_data_str):
    """
    Check if a repository URL is already in the database using case-insensitive string matching.
    
    Parameters
    ----------
    repo_url : str
        URL of the repository to check.
    existing_data_str : str
        String representation of existing data.
    
    Returns
    -------
    bool
        True if the repository is already in the database, False otherwise.
    """
    # Normalize URL (remove trailing slash, convert to lowercase)
    normalized_url = repo_url.rstrip('/').lower()
    
    # Also check without https://
    url_variations = [
        normalized_url,
        normalized_url.replace('https://', ''),
        normalized_url.replace('https://github.com/', '')
    ]
    
    existing_data_lower = existing_data_str.lower()
    
    for url_var in url_variations:
        if url_var in existing_data_lower:
            return True
    
    return False


def main():
    """
    Main function to scan GitHub organizations and add new repositories.
    """
    repository = sys.argv[1] if len(sys.argv) > 1 else "scads/zenodo-tracking"
    
    yml_filename = "resources/scadsai.yml"
    
    # Load existing data
    print("Loading existing database...")
    df = load_dataframe("resources/")
    existing_data_str = str(df.to_dict())
    
    # Load organizations
    print("Loading organizations...")
    organizations = load_organizations()
    print(f"Found {len(organizations)} organizations to scan")
    
    # Collect new repositories
    new_repos = []
    log = []
    
    for org_name in organizations:
        log.append(f"## Organization: {org_name}")
        log.append(f"https://github.com/{org_name}")
        log.append("")
        
        repos = get_organization_repos(org_name)
        
        for repo_info in repos:
            repo_url = repo_info['url']
            
            # Check if already in database
            if not is_repo_in_database(repo_url, existing_data_str):
                print(f"  New repository found: {repo_url}")
                
                # Get full metadata
                metadata = get_repo_metadata(repo_url)
                if metadata:
                    new_repos.append(metadata)
                    log.append(f"* [{metadata['name']}]({repo_url}) - {repo_info['stars']} stars")
                    
                    # Update existing_data_str to avoid duplicates in the same run
                    existing_data_str += " " + repo_url
            else:
                print(f"  Already in database: {repo_url}")
        
        log.append("")
    
    if not new_repos:
        print("No new repositories found.")
        return
    
    print(f"\nFound {len(new_repos)} new repositories")
    
    # Create branch and prepare pull request
    branch = create_branch(repository)
    print(f"Created branch: {branch}")
    
    # Convert new repos to YAML
    new_data_yaml = yaml.dump(new_repos, default_flow_style=False, allow_unicode=True)
    
    # Get existing file content
    file_content = get_file_in_repository(repository, branch, yml_filename).decoded_content.decode()
    
    # Append new data
    file_content += new_data_yaml
    
    # Write back to GitHub
    commit_message = f"Add {len(new_repos)} repositories from organization scan"
    write_file(repository, branch, yml_filename, file_content, commit_message)
    
    # Create pull request
    log_text = "\n".join(log)
    pr_title = f"Add {len(new_repos)} repositories from GitHub organizations"
    pr_body = f"Automatically discovered repositories from configured GitHub organizations:\n\n{log_text}"
    
    result = send_pull_request(repository, branch, pr_title, pr_body)
    
    print(f"Done. {result}")


if __name__ == "__main__":
    main()
