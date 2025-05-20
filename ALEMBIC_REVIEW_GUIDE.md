# Using Alembic Review Tool

This guide explains how to use the `alembic-review` tool from [OpenMindUA/alembic-actions](https://github.com/OpenMindUA/alembic-actions) to validate your Alembic migrations.

## Installation

Install the tool directly from GitHub:

```bash
pip install git+https://github.com/OpenMindUA/alembic-actions.git@v1
```

## Command Line Usage

After installation, you can run the `alembic-review` command:

```bash
alembic-review --alembic-ini-path alembic.ini --target-branch main \
  --check-revision-files \
  --check-revision-order \
  --check-downgrade \
  --check-upgrade \
  --check-duplicate-ops
```

### Available Options

- `--alembic-ini-path`: Path to your alembic.ini file (default: alembic.ini)
- `--target-branch`: Branch to compare migrations against (default: main)
- `--migration-script-path`: Path to migration scripts (default: derived from alembic.ini)
- `--check-revision-files`: Verify revision files exist and are valid
- `--check-revision-order`: Verify migrations are ordered correctly
- `--check-downgrade`: Test downgrade operations
- `--check-upgrade`: Test upgrade operations
- `--check-duplicate-ops`: Check for duplicate operations

## Using with GitHub Actions

Add the following to your GitHub Actions workflow file:

```yaml
jobs:
  check-migrations:
    runs-on: ubuntu-latest
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

      - name: Install alembic-review
        run: |
          pip install git+https://github.com/OpenMindUA/alembic-actions.git@v1
          
      - name: Check Alembic Migrations
        run: |
          # Determine the base branch
          BASE_BRANCH="main"
          if ! git ls-remote --exit-code --heads origin main; then
            BASE_BRANCH="master"
          fi
          
          # Run the alembic-review command
          PYTHONPATH=$PYTHONPATH:$(pwd) alembic-review \
            --alembic-ini-path alembic.ini \
            --target-branch $BASE_BRANCH \
            --check-revision-files \
            --check-revision-order \
            --check-downgrade \
            --check-upgrade \
            --check-duplicate-ops
```

## Using the Helper Script

This repository includes a helper script `check_migrations.py` to simplify running migration checks:

```bash
# Run all checks
./check_migrations.py --check-all

# Run with custom options
./check_migrations.py --alembic-ini-path ./alembic.ini --target-branch develop --verbose
```