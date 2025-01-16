"""
Crate resuable functions for databse operations.
"""

import psycopg2

from config import DB_CONFIG

def get_connection():
    """Establish and return connection to PostgrSQL database."""
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        return connection
    except psycopg2.error as e:
        print(f"Error connecting to the database: {e}")
        raise
