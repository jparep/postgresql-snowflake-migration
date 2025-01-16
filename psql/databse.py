"""
Crate resuable functions for databse operations.
"""

import pysycopg2
from config import DB_CONFIG

def get_connection():
    """Establish and return connection to PostgrSQL database."""
    try:
        connection = pysycopg2.connect(**DB_CONFIG)
        return connection
    except pysycopg2.error as e:
        print("Error connecting to the database:" e)
        raise
