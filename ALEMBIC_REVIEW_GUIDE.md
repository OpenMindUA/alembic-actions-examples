# Using Alembic Review GitHub Action

This guide explains how to use the `alembic-review` GitHub Action from [OpenMindUA/alembic-actions](https://github.com/OpenMindUA/alembic-actions) to validate your Alembic migrations.

## Using with GitHub Actions

Add the following to your GitHub Actions workflow file:

```yaml
jobs:
  check-migrations:
    runs-on: ubuntu-latest
    # These permissions are needed for PR comments
    permissions:
      contents: read
      pull-requests: write
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Check Alembic Migrations
        uses: OpenMindUA/alembic-actions/actions/alembic-review@v1
        with:
          # Relative path to the alembic.ini file
          alembic_ini_path: 'alembic.ini'

          # Checks to be performed (all enabled by default)
          check_revision_files: 'true'
          check_revision_order: 'true'
          check_downgrade: 'true'
          check_upgrade: 'true'
          check_duplicate_ops: 'true'

          # Additional optional configurations
          # target_branch: 'main'  # Base branch to compare against (default: main or master)
          # migration_script_path: 'migrations' # Path to the migrations directory (default: derived from alembic.ini)
```

## Required Permissions

The GitHub Action requires specific permissions to function properly:

```yaml
permissions:
  contents: read    # Needed to read repository contents
  pull-requests: write  # Needed to comment on pull requests
```

These permissions allow the action to post comments on pull requests with the results of the migration validation.

## Available Options

The GitHub Action supports the following parameters:

- `alembic_ini_path`: Path to your alembic.ini file (default: alembic.ini)
- `target_branch`: Branch to compare migrations against (default: main or master)
- `migration_script_path`: Path to migration scripts (default: derived from alembic.ini)
- `check_revision_files`: Verify revision files exist and are valid (default: true)
- `check_revision_order`: Verify migrations are ordered correctly (default: true)
- `check_downgrade`: Test downgrade operations (default: true)
- `check_upgrade`: Test upgrade operations (default: true)
- `check_duplicate_ops`: Check for duplicate operations (default: true)

## Local Testing with alembic-review

For local testing and development purposes, you can still use the command-line version of alembic-review. This approach is helpful for debugging issues before pushing to GitHub.

### Installation

```bash
pip install git+https://github.com/OpenMindUA/alembic-actions.git@v1
```

### Command Line Usage

```bash
alembic-review --alembic-ini-path alembic.ini --target-branch main \
  --check-revision-files \
  --check-revision-order \
  --check-downgrade \
  --check-upgrade \
  --check-duplicate-ops
```