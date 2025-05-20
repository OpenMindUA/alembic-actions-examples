#!/usr/bin/env python3
"""
Simple script to demonstrate running Alembic migrations
"""
import subprocess
import os

def run_migrations():
    """Run Alembic migrations to latest version"""
    print("Running database migrations...")
    try:
        subprocess.run(["alembic", "upgrade", "head"], check=True)
        print("Migrations completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error running migrations: {e}")
        exit(1)

def check_migrations():
    """Check if there are any new migrations that need to be applied"""
    print("Checking for unapplied migrations...")
    result = subprocess.run(
        ["alembic", "current"],
        check=True,
        capture_output=True,
        text=True
    )
    
    result2 = subprocess.run(
        ["alembic", "heads"],
        check=True,
        capture_output=True,
        text=True
    )
    
    current = result.stdout.strip()
    head = result2.stdout.strip()
    
    if current != head:
        print(f"Database is at version {current}")
        print(f"Latest available version is {head}")
        print("There are unapplied migrations!")
        return False
    else:
        print("Database is up to date.")
        return True

if __name__ == "__main__":
    # Check if this is being run to apply migrations or just check them
    if len(os.sys.argv) > 1 and os.sys.argv[1] == "--check":
        is_current = check_migrations()
        if not is_current:
            exit(1)
    else:
        run_migrations()