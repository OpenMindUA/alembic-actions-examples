#!/usr/bin/env python3
"""
Test script to verify Alembic migrations
"""
import os
import unittest
import subprocess
import sqlite3

class TestAlembicMigrations(unittest.TestCase):
    """Test case for verifying Alembic migrations"""
    
    DB_FILE = "./test.db"
    
    def setUp(self):
        """Set up test environment by removing existing database"""
        # Remove the test database if it exists
        if os.path.exists(self.DB_FILE):
            os.remove(self.DB_FILE)
    
    def _run_alembic_command(self, *args):
        """Run an Alembic command and return its output"""
        cmd = ["alembic"] + list(args)
        result = subprocess.run(
            cmd, 
            check=True,
            capture_output=True,
            text=True
        )
        return result.stdout
    
    def test_migrations(self):
        """Test that all migrations apply successfully"""
        # Run the first migration (users table)
        self._run_alembic_command("upgrade", "69be7091e340")
        
        # Verify the users table exists
        conn = sqlite3.connect(self.DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        self.assertEqual(cursor.fetchone()[0], "users")
        
        # Verify the columns in the users table
        cursor.execute("PRAGMA table_info(users)")
        columns = [row[1] for row in cursor.fetchall()]
        self.assertIn("id", columns)
        self.assertIn("username", columns)
        self.assertIn("email", columns)
        self.assertIn("is_active", columns)
        self.assertIn("created_at", columns)
        
        # Run the second migration (posts table)
        self._run_alembic_command("upgrade", "2e6c867ebffd")
        
        # Verify the posts table exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='posts'")
        self.assertEqual(cursor.fetchone()[0], "posts")
        
        # Verify the columns in the posts table
        cursor.execute("PRAGMA table_info(posts)")
        columns = [row[1] for row in cursor.fetchall()]
        self.assertIn("id", columns)
        self.assertIn("title", columns)
        self.assertIn("content", columns)
        self.assertIn("user_id", columns)
        self.assertIn("created_at", columns)
        self.assertIn("updated_at", columns)
        
        # Test downgrade
        self._run_alembic_command("downgrade", "69be7091e340")
        
        # Verify the posts table is gone
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='posts'")
        self.assertIsNone(cursor.fetchone())
        
        # Verify the users table still exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        self.assertEqual(cursor.fetchone()[0], "users")
        
        # Test full downgrade
        self._run_alembic_command("downgrade", "base")
        
        # Verify the users table is gone
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
        self.assertIsNone(cursor.fetchone())
        
        conn.close()

if __name__ == "__main__":
    unittest.main()