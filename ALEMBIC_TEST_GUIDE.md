# Using Alembic Test GitHub Action

This guide explains how to use the `alembic-test` GitHub Action from [OpenMindUA/alembic-actions](https://github.com/OpenMindUA/alembic-actions) to thoroughly test your Alembic migrations.

## Alembic Test vs Alembic Review

The OpenMindUA/alembic-actions repository provides two complementary actions:

1. **alembic-review**: Focuses on code review aspects of migrations
   - Checks revision files existence and validity
   - Verifies migration ordering
   - Tests basic upgrade/downgrade operations 
   - Detects duplicate operations
   - Perfect for quick validation during code reviews

2. **alembic-test**: Provides more comprehensive testing of migrations
   - Runs actual migrations against a test database
   - Verifies single head compliance (no branch conflicts)
   - Tests all upgrade paths
   - Tests all downgrade paths
   - Validates model definitions against migration scripts
   - More suitable for thorough testing of migration functionality

## Using with GitHub Actions

Add the following to your GitHub Actions workflow file:

```yaml
jobs:
  test-migrations:
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
          pip install pytest pytest-alembic

      - name: Test Alembic Migrations
        uses: OpenMindUA/alembic-actions/actions/alembic-test@v1
        with:
          # Database configuration
          dialect: 'sqlite'  # Database dialect to use
          alembic_ini: 'alembic.ini'  # Path to alembic.ini file
          migration_path: 'migrations'  # Path to migration scripts
          database_url: 'sqlite:///./test_migrations.db'  # Database URL for testing
          # test_data_script: ''  # Optional script to load test data
```

## Required Permissions

The GitHub Action requires specific permissions to function properly:

```yaml
permissions:
  contents: read    # Needed to read repository contents
  pull-requests: write  # Needed to comment on pull requests
```

These permissions allow the action to post comments on pull requests with the test results.

## Available Options

The GitHub Action supports the following parameters:

- `dialect`: Database dialect to use (e.g., 'sqlite', 'postgresql', 'mysql')
- `alembic_ini`: Path to your alembic.ini file (default: alembic.ini)
- `migration_path`: Path to migration scripts (default: derived from alembic.ini)
- `database_url`: Database URL for testing (default: sqlite:///:memory:)
- `test_data_script`: Optional path to a script that loads test data

## Local Testing

For local testing, you can use pytest-alembic directly:

```bash
# Install pytest-alembic
pip install pytest-alembic

# Run basic tests
pytest --alembic-config=alembic.ini

# Run comprehensive tests
pytest --alembic-config=alembic.ini \
  --test-single-head \
  --test-upgrades \
  --test-downgrades \
  --test-model-definitions
```

## Recommended Usage Pattern

For a complete Alembic migration validation setup, we recommend:

1. Use **alembic-review** for quick checks during the PR process
2. Use **alembic-test** for more thorough validation before merging
3. Run both actions to ensure your migrations are both well-formatted and functionally correct