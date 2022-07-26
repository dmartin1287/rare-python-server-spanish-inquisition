import sqlite3
import json

from models import Category

def get_all_categories():
    """ Gets all categories from the database

    Returns:
        string: JSON serialized string of the contents of the categories table
    """
    with sqlite3.connect("./db.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            c.id,
            c.label
        FROM Categories c
        """)

        categories = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            category = Category(row['id'], row['label'])

            categories.append(category.__dict__)

    return json.dumps(categories)
