"""Create the database and add a few safe example products."""

import sqlite3
from pathlib import Path

from database import DATABASE_PATH

PROJECT_FOLDER = Path(__file__).parent

EXAMPLE_PRODUCTS = [
    ("Canvas Bag", "A reusable bag for everyday shopping.", 12.99, 6.25, 20, 1),
    ("Coffee Mug", "A simple ceramic mug.", 8.50, 3.10, 15, 1),
    ("Notebook", "An A5 lined notebook.", 5.25, 1.80, 30, 1),
]


def seed_database():
    """Create tables and insert examples when the catalogue is empty."""
    schema = (PROJECT_FOLDER / "schema.sql").read_text(encoding="utf-8")

    with sqlite3.connect(DATABASE_PATH) as database:
        database.executescript(schema)
        product_count = database.execute("SELECT COUNT(*) FROM products").fetchone()[0]

        if product_count == 0:
            database.executemany(
                """
                INSERT INTO products
                    (name, description, selling_price, cost_price, stock, active)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                EXAMPLE_PRODUCTS,
            )
            print("Added example products.")
        else:
            print("Products already exist; no examples were added.")

    print(f"Database ready at {DATABASE_PATH}")


if __name__ == "__main__":
    seed_database()
