# This script is executed when a new issue is created on our github repository. 
# In case the issue text consists only of a single line starting like a zenodo link, 
# it will retrieve all important details from the zenodo record, add it to a yml file
# and send a pull-request
import sys
from _github_utilities import create_branch, get_file_in_repository, get_issue_body, write_file, send_pull_request
import yaml
from datetime import datetime
from generate_link_lists import (complete_zenodo_data, all_content,
                                  find_parent_entry, merge_zenodo_entry)

def main():
    """
    Main function to handle the process of retrieving Zenodo data and appending
    it to a YAML file in a GitHub repository.

    This function takes command-line arguments for the repository name and issue number,
    retrieves the issue body, checks if it's a valid Zenodo link, retrieves corresponding
    data, and appends it to a specified YAML file by creating a new branch and submitting
    a pull request.

    When a submitted URL belongs to the same Zenodo concept as an existing entry
    (i.e. it is a new version of something already tracked), the existing entry
    is updated in-place rather than creating a duplicate.

    Returns
    -------
    None
    """
    repository = sys.argv[1]
    issue = int(sys.argv[2])
    
    yml_filename = "resources/scadsai.yml"
    
    issue_text = get_issue_body(repository, issue)
    zenodo_urls = [line for line in issue_text.splitlines() if line.startswith("https://zenodo.org/records")]
    
    if not zenodo_urls:
        print(issue_text, " does not contain any zenodo link. I show myself out.")
        return

    # read "database"
    branch = create_branch(repository)
    file_content_str = get_file_in_repository(repository, branch, yml_filename).decoded_content.decode()
    print("yml file content length:", len(file_content_str))

    # Parse the YAML file so we can update existing entries when needed
    file_data = yaml.safe_load(file_content_str)
    if file_data is None:
        file_data = {'resources': []}

    # Load all resources for cross-file parent detection
    resources_dir = yml_filename.rsplit('/', 1)[0] + '/'
    existing_resources = all_content(resources_dir)['resources']
    all_urls_set = set()
    for r in existing_resources:
        urls = r.get('url', [])
        if isinstance(urls, str):
            urls = [urls]
        all_urls_set.update(urls)

    pr_notes = []

    for zenodo_url in zenodo_urls:
        # read data from zenodo
        new_data = complete_zenodo_data(zenodo_url)

        if isinstance(new_data.get("url"), str):
            new_data["url"] = [new_data["url"]]

        # Skip if URL is already tracked
        if any(u in all_urls_set for u in new_data.get("url", [])):
            msg = f"Already tracked: {zenodo_url}"
            print(msg)
            pr_notes.append(f"* Skipped (already tracked): {zenodo_url}")
            continue

        conceptrecid = new_data.get('conceptrecid')

        # Check whether this is a new version of an already-tracked record
        parent = find_parent_entry(file_data['resources'], conceptrecid)

        if parent is not None:
            # Merge new-version metadata into the existing entry
            merge_zenodo_entry(parent, new_data)
            msg = f"  -> merged as new version of existing entry '{parent.get('name')}'"
            print(msg)
            pr_notes.append(f"* Updated existing entry (new version): [{new_data.get('name', zenodo_url)}]({zenodo_url})")
        else:
            # Check all resources (other yml files) to avoid cross-file duplicates
            parent_other = find_parent_entry(existing_resources, conceptrecid)
            if parent_other is not None:
                msg = f"  -> parent found in a different file for {zenodo_url}, skipping duplicate"
                print(msg)
                pr_notes.append(f"* Skipped (parent entry found in another file): [{new_data.get('name', zenodo_url)}]({zenodo_url})")
            else:
                # Genuinely new entry
                file_data['resources'].append(new_data)
                existing_resources.append(new_data)
                pr_notes.append(f"* Added: [{new_data.get('name', zenodo_url)}]({zenodo_url})")

        for u in new_data.get("url", []):
            all_urls_set.add(u)

    # save back to github
    new_file_content = yaml.dump(file_data, allow_unicode=True)
    write_file(repository, branch, yml_filename, new_file_content, "Add multiple Zenodo entries")
    pr_body = f"closes #{issue}\n\n" + "\n".join(pr_notes)
    res = send_pull_request(repository, branch, "Add multiple Zenodo entries", pr_body)

    print("Done.", res)
    

if __name__ == "__main__":
    main()
