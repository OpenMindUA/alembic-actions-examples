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