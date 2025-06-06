"""
Database initialization module for the Smart Band project.
This module sets up the SQLite database connection and initializes the database.
"""

from peewee import SqliteDatabase



# Define the database connection
db = SqliteDatabase('smart_band.db')


def init_db() -> None:
    """Initialize the database and create tables if they do not exist."""
    db.connect()
    from iam.infrastructure.models import Device
    db.create_tables([Device], safe=True)  # Add your models here
    print("Database initialized.")
    db.close()