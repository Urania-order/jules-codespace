"""
Pytest configuration for smos tests.

Forces SQLite in-memory database for tests when PostgreSQL
is not available. This makes tests independent of external
infrastructure.
"""
import os

# Use SQLite for tests unless DATABASE_URL is explicitly set
if "DATABASE_URL" not in os.environ:
    os.environ["DATABASE_URL"] = "sqlite:///:memory:"

# Allow SQLAlchemy 2.0 compatibility
os.environ.setdefault("SQLALCHEMY_SILENCE_UBER_WARNING", "1")
