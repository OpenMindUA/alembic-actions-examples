# Alembic Actions Example

This is a simple example application demonstrating Alembic database migrations for testing the [OpenMindUA/alembic-actions](https://github.com/OpenMindUA/alembic-actions) GitHub workflow.

## Project Structure

```
.
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py   # User SQLAlchemy model
│   ├── __init__.py
│   └── database.py   # SQLAlchemy database configuration
├── migrations/       # Alembic migrations directory
├── alembic.ini       # Alembic configuration
├── README.md
└── requirements.txt  # Python dependencies
```

## Setup

1. Create a virtual environment and install dependencies:
   ```
   uv venv
   source .venv/bin/activate
   uv pip install -r requirements.txt
   ```

2. Run migrations:
   ```
   alembic upgrade head
   ```

## Migration Examples

- Initial migration creates the `users` table
- Additional migrations can be added to demonstrate schema changes

## Testing Alembic Actions

This repository is designed to test the functionality of the [OpenMindUA/alembic-actions](https://github.com/OpenMindUA/alembic-actions) GitHub workflow, which automates checks for Alembic migrations during pull requests.

### GitHub Actions Included

This repository demonstrates the use of two complementary GitHub Actions from the OpenMindUA/alembic-actions repository:

1. **alembic-review**: Code review focused validation ([workflow](.github/workflows/alembic-check.yml))
   - Checks revision files existence and formatting
   - Verifies migration ordering
   - Quick validation ideal for PR reviews
   - [See detailed guide](ALEMBIC_REVIEW_GUIDE.md)

2. **alembic-test**: Comprehensive migration testing ([workflow](.github/workflows/alembic-test.yml))
   - Runs migrations against a test database
   - Tests all upgrade and downgrade paths
   - Validates model definitions
   - [See detailed guide](ALEMBIC_TEST_GUIDE.md)

3. **Migration application workflow**: Example of applying migrations ([workflow](.github/workflows/apply-migrations.yml))
   - Demonstrates how to safely apply migrations in a CI/CD pipeline
   - Includes validation before applying
   - Shows notification patterns for team communication