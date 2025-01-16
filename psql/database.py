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

def excute_query(query, data=None):
    """Excecute a query with optionsal parameters."""
    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
    except psycopg2.Error as e:
        print(f"Error executing query: {e}")
        connection.rollback()
    finally:
        cursor.close()
        connection.close()
