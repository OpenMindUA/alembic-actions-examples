#!/usr/bin/env python3
"""
Command-line tool to check Alembic migrations using alembic-review
"""
import argparse
import subprocess
import sys
import os

def main():
    parser = argparse.ArgumentParser(description='Check Alembic migrations')
    parser.add_argument('--alembic-ini-path', default='alembic.ini',
                        help='Path to alembic.ini file')
    parser.add_argument('--target-branch', default='main',
                        help='Target branch to compare migrations against')
    parser.add_argument('--check-all', action='store_true',
                        help='Run all checks')
    parser.add_argument('--verbose', '-v', action='store_true',
                        help='Verbose output')
    
    args = parser.parse_args()
    
    # Check if alembic-review is installed
    try:
        import importlib.util
        if importlib.util.find_spec("alembic_review") is None:
            print("alembic-review is not installed. Installing...")
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", 
                "git+https://github.com/OpenMindUA/alembic-actions.git@v1"
            ])
    except ImportError:
        print("Could not check if alembic-review is installed. Attempting to install...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", 
            "git+https://github.com/OpenMindUA/alembic-actions.git@v1"
        ])
    
    # Build the command
    cmd = [
        "alembic-review",
        "--alembic-ini-path", args.alembic_ini_path,
        "--target-branch", args.target_branch,
    ]
    
    if args.check_all:
        cmd.extend([
            "--check-revision-files",
            "--check-revision-order",
            "--check-downgrade",
            "--check-upgrade",
            "--check-duplicate-ops"
        ])
    
    if args.verbose:
        cmd.append("--verbose")
    
    # Set PYTHONPATH to include current directory
    env = os.environ.copy()
    env["PYTHONPATH"] = f"{env.get('PYTHONPATH', '')}:{os.getcwd()}"
    
    print(f"Running command: {' '.join(cmd)}")
    
    try:
        subprocess.run(cmd, check=True, env=env)
        print("All migration checks passed!")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"Migration checks failed with exit code {e.returncode}")
        return e.returncode

if __name__ == "__main__":
    sys.exit(main())