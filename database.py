"""Small helpers for opening and closing the MiniMart database."""

import sqlite3
from pathlib import Path

from flask import g

DATABASE_PATH = Path(__file__).parent / "minimart.db"


def get_db():
    """Open one database connection for the current web request."""
    if "database" not in g:
        g.database = sqlite3.connect(DATABASE_PATH)
        g.database.row_factory = sqlite3.Row
        g.database.execute("PRAGMA foreign_keys = ON")
    return g.database


def close_db(_error=None):
    """Close the connection after Flask finishes the request."""
    database = g.pop("database", None)
    if database is not None:
        database.close()


def init_app(app):
    """Tell Flask to close the database after every request."""
    app.teardown_appcontext(close_db)
