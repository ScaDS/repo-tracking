# Agent Analysis: Zenodo Tracking Repository

## Repository Overview

This repository maintains a searchable collection of Zenodo and GitHub resources created by ScaDS.AI members. It automatically aggregates, tracks, and publishes materials through a Jupyter Book website hosted at https://scads.github.io/zenodo-tracking.

## Core Architecture

The system consists of automated scripts that:
1. Collect resources from multiple sources (Zenodo communities, GitHub issues)
2. Track download and engagement statistics
3. Generate structured documentation
4. Maintain data consistency through YAML storage

## File Analysis

### Main Scripts

#### `scripts/generate_link_lists.py` (534 lines)
**Purpose**: Central content generation engine for the Jupyter Book

**Key Functions**:
- `main()`: Orchestrates the entire documentation generation process
  - Reads all YAML resource files from `resources/` directory
  - Generates markdown pages organized by domain, content type, tags, licenses, and authors
  - Creates a "What's New" page with recently added items
  - Detects duplicate entries and enforces data integrity
  - Updates table of contents (`docs/_toc.yml`) and statistics in `docs/readme.md`
  
- `all_content(directory_path)`: Aggregates all resources from YAML files into a single dictionary
- `load_dataframe(directory_path)`: Converts all resources into a pandas DataFrame
- `read_zenodo(record)`: Fetches metadata from Zenodo API
- `read_github_license(github_url)`: Retrieves license information from GitHub API
- `update_yaml_file(yaml_filename)`: Updates YAML entries with latest Zenodo/GitHub metadata
- `collect_all(content, what_to_collect)`: Counts occurrences of specific attributes (tags, licenses, authors, etc.)
- `find_*()` functions: Filter resources by author, license, type, tag, or domain
- `write_md(resources, title, filename)`: Generates markdown documentation pages
- `complete_zenodo_data(zenodo_url)`: Retrieves and structures complete Zenodo record metadata

**Integration**: Called by CI/CD before building the Jupyter Book, generates all dynamic content.

---

#### `scripts/auto-add-zenodo-entry.py` (108 lines)
**Purpose**: Automated workflow for adding Zenodo entries via GitHub issues

**Workflow**:
1. Triggered when a GitHub issue is created containing Zenodo URLs
2. Validates issue contains `https://zenodo.org/records` links
3. Creates a new branch in the repository
4. Fetches complete metadata from Zenodo API using `complete_zenodo_data()`
5. Appends new entries to `resources/scadsai.yml`
6. Creates a pull request with the changes
7. Closes the originating issue

**Key Functions**:
- `main()`: Entry point, processes command-line arguments (repository, issue number)
- `complete_zenodo_data(zenodo_url)`: Extracts title, authors, description, license, publication date, DOI, and download statistics

**Usage**: `python auto-add-zenodo-entry.py <repository> <issue_number>`

---

#### `scripts/auto-add-from-zenodo-communities.py` (108 lines)
**Purpose**: Automatically discovers and adds new content from Zenodo communities

**Workflow**:
1. Queries Zenodo API for records in configured communities (e.g., 'scads-ai')
2. Compares with existing database to identify new entries
3. Retrieves full metadata for new records
4. Appends to YAML database with submission timestamps
5. Creates pull request with summary of added materials

**Key Features**:
- Handles multiple communities in a single run
- Prevents duplicate entries by checking URLs against existing data
- Adds ISO-formatted submission dates
- Generates detailed PR descriptions listing all additions

**Configuration**: Uses `ZENODO_API_KEY` environment variable for authentication

---

#### `scripts/auto-add-github-resources.py` (163 lines)
**Purpose**: Processes GitHub repository submissions via issues

**Workflow**:
1. Triggered by GitHub issue containing `https://github.com/` URLs
2. Extracts repository metadata using GitHub API
3. Retrieves contributor information (full names when available)
4. Fetches repository statistics (stars, forks)
5. Extracts license information
6. Generates formatted YAML entry
7. Creates pull request with changes

**Key Functions**:
- `main()`: Handles multi-line issues with multiple GitHub URLs
- `complete_github_data(github_repo_url)`: Comprehensive metadata extraction including:
  - Contributors with full names
  - Repository description
  - Topics/tags
  - License
  - Creation date
  - Default branch
  - Homepage URL

**Authentication**: Requires `GITHUB_API_KEY` environment variable

---

#### `scripts/auto-add-github-statistics.py` (~80 lines)
**Purpose**: Tracks GitHub repository engagement metrics over time

**Workflow**:
1. Scans all resources in YAML files for GitHub URLs
2. Extracts repository identifiers (owner/repo)
3. Queries GitHub API for current statistics:
   - Star count
   - Fork count
4. Generates dated CSV file in `github_statistics/YYYYMMDD.csv`
5. Creates pull request with the statistics file

**Key Functions**:
- `extract_github_repos(yaml_data)`: Parses YAML to find GitHub repository URLs
- `get_repo_stats(repo_name)`: Fetches current engagement metrics
- Stores historical data for trend analysis

**Output Format**: CSV with columns: repo_name, stars, forks

---

#### `scripts/auto-add-download-statistics.py` (132 lines)
**Purpose**: Scheduled collection of Zenodo download statistics

**Schedule**: Runs every Monday at 11 AM (via automation)

**Workflow**:
1. Iterates through all resources in YAML database
2. For each Zenodo URL:
   - Converts DOI URLs to records format if needed
   - Fetches statistics from Zenodo API
3. Compiles DataFrame with:
   - URL
   - Authors
   - Downloads (total)
   - Unique downloads
   - Views
   - Unique views
   - Version count
4. Saves as `download_statistics/YYYYMMDD.csv`
5. Creates pull request with statistics file

**Key Functions**:
- `summarize_download_statistics(directory_path)`: Main aggregation logic
- Handles URL normalization (DOI → records format)
- Exports comprehensive engagement metrics

**Output**: Time-series data enabling trend analysis of resource usage

---

#### `scripts/_github_utilities.py` (214 lines)
**Purpose**: Shared utility library for GitHub API interactions

**Core Utilities**:
- `get_github_repository(repository)`: Authenticated repository access (cached)
- `get_issue_body(repository, issue)`: Retrieve issue content
- `write_file(repository, branch_name, file_path, new_content, commit_message)`: Create/update files with atomic commits
- `get_file_in_repository(repository, branch_name, file_path)`: Cached file retrieval
- `create_branch(repository, parent_branch)`: Generate random branch names for PRs
- `check_if_file_exists(repository, branch_name, file_path)`: File existence validation
- `send_pull_request(repository, branch_name, title, description)`: PR creation with issue linking

**Architecture Features**:
- Uses `@lru_cache` for performance optimization
- Adapted from git-bob project (LGPL3 licensed)
- Centralized authentication via `GITHUB_API_KEY` environment variable
- Random branch naming: `git-bob-mod-{10_char_random}`

---

### Notebooks

#### `notebooks/download_stats.ipynb`
**Purpose**: Interactive analysis of Zenodo download statistics

**Functions**:
- `read_file_and_date(filename)`: Loads CSV files with date extraction from filename
- `get_title_of_zenodo_record(url)`: Retrieves human-readable titles for visualizations
- `get_tag(url)`: Extracts categorization tags for filtering

**Capabilities**: Time-series visualization, trend analysis, comparative statistics across resources

---

#### `notebooks/slide_counting.ipynb`
**Purpose**: Analyzes presentation materials hosted on Zenodo

**Functions**:
- `get_zenodo_files(zenodo_url)`: Downloads file listings from Zenodo records
- `count_slides(file_path)`: Analyzes PDF files to count presentation slides

**Use Cases**: Assessing training material scope, tracking content volume

---

### Configuration Files

#### `resources/scadsai.yml`
**Structure**: Primary database file containing resource entries

**Entry Schema**:
```yaml
- authors: [list of names]
  description: "Full text description"
  license: "SPDX license identifier"
  name: "Resource title"
  num_downloads: integer
  publication_date: "YYYY-MM-DD"
  submission_date: "ISO 8601 timestamp"
  url: [list of URLs - Zenodo, DOI, GitHub]
  tags: [optional - list of keywords]
  type: "optional - content type"
```

#### `requirements.txt`
**Key Dependencies**:
- `jupyter-book==1.0.3`: Static site generation
- `pygithub`: GitHub API wrapper
- `pandas`: Data manipulation
- `pypdfium2`: PDF processing for slide counting
- `transformers`: AI/ML capabilities (future use)

---

### Documentation Structure

#### `docs/`
Jupyter Book source with generated content:
- `_toc.yml`: Auto-generated table of contents with placeholders
- `readme.md`: Main page with statistics (`{number_of_links}`, `{last_updated}`)
- `domain/`: Auto-generated pages organized by source domain
- `content_types/`: Pages categorized by resource type
- `tags/`: Tag-based organization
- `licenses/`: License-based filtering
- `authors/`: Author attribution pages
- `export/`: Data export functionality documentation
- `statistics/`: Usage analytics documentation

---

## Automation Workflows

### Issue-Based Submission
1. User creates GitHub issue with URL
2. Repository automation detects issue type (Zenodo vs GitHub)
3. Appropriate script fetches metadata
4. Pull request created with structured YAML entry
5. Maintainer reviews and merges
6. Static site regenerates with new content

### Scheduled Statistics Collection
1. Weekly cron job triggers statistics scripts
2. Current metrics collected from APIs
3. Historical CSV files committed
4. Enables longitudinal analysis of resource impact

### Community Monitoring
1. Periodic check of Zenodo communities
2. New submissions auto-detected
3. Batch pull requests created
4. Ensures comprehensive coverage

---

## Data Flow

```
Sources → Scripts → YAML Database → generate_link_lists.py → Markdown Files → Jupyter Book → Static Site
  ↓                                                                                         ↑
  └─ Statistics Scripts → CSV Files ──────────────────────────────────────────────────────┘
```

---

## Key Design Patterns

1. **Declarative Data Storage**: YAML as single source of truth
2. **Automation via GitHub Actions**: Event-driven and scheduled workflows
3. **Metadata Enrichment**: Automatic population from authoritative APIs
4. **Pull Request Review**: Human validation before publication
5. **Time-Series Tracking**: Historical statistics for impact analysis
6. **Duplicate Prevention**: URL-based deduplication in generation script
7. **Modular Architecture**: Shared utilities via `_github_utilities.py`

---

## Environment Requirements

**Required Environment Variables**:
- `GITHUB_API_KEY`: GitHub API authentication token
- `ZENODO_API_KEY`: Zenodo API access token (optional for public records)

**Execution Context**:
- Scripts designed for GitHub Actions runners
- Command-line arguments: `<repository>` and `<issue_number>`
- File system access to `resources/` directory

---

## Extension Points

### Adding New Sources
1. Create new `auto-add-*.py` script following existing patterns
2. Use `_github_utilities.py` for GitHub integration
3. Format output as YAML matching schema
4. Create pull request with changes

### New Organization Dimensions
1. Add collection logic in `collect_all()`
2. Create finder function (`find_*()`)
3. Add generation loop in `main()`
4. Update `_toc.yml` placeholder

### Custom Analytics
1. Add script to generate CSV in appropriate directory
2. Use `all_content()` to load resource database
3. Follow existing PR creation patterns
4. Notebook analysis can reference new data files

---

## Quality Assurance

- **Duplicate Detection**: `generate_link_lists.py` raises `KeyError` on duplicates
- **URL Normalization**: Handles DOI vs records URLs consistently
- **Minimum Item Threshold**: Pages only generated for categories with ≥5 items
- **API Error Handling**: Try-except blocks with graceful degradation
- **Branch Isolation**: All changes through pull requests, never direct commits

---

## Licensing & Attribution

- **Repository Content**: CC-BY 4.0
- **Utilities**: Adapted from git-bob project (LGPL3)
- **Dependencies**: Various open-source licenses (see requirements.txt)

---

## Recommended Agent Actions

### For Content Addition Agents
1. Use `auto-add-zenodo-entry.py` or `auto-add-github-resources.py`
2. Validate URL format before submission
3. Check for existing entries to prevent duplicates
4. Include descriptive PR messages

### For Analytics Agents
1. Read CSV files in `download_statistics/` and `github_statistics/`
2. Use notebooks for exploratory analysis
3. Load full dataset via `generate_link_lists.load_dataframe('resources/')`

### For Maintenance Agents
1. Run `update_yaml_file()` to refresh metadata
2. Execute `generate_link_lists.py` to rebuild documentation
3. Monitor for API rate limits and authentication issues
4. Review PR descriptions for quality control

---

## Future Considerations

- Transform detection system mentioned in requirements (`transformers` package)
- Export functionality (referenced in docs but not fully implemented)
- GDPR compliance documentation exists but implementation unclear
- Potential for federated search across multiple AI center indices
