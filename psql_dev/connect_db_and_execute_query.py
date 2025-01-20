"""
Create reusable functions for database operations.
"""

import psycopg2
from psycopg2.extras import RealDictCursor
from config import DB_CONFIG


def get_connection(config=None):
    """
    Establish and return a connection to the PostgreSQL database.

    Args:
        config (dict, optional): Database configuration dictionary. Defaults to DB_CONFIG.

    Returns:
        psycopg2.connection: A connection object to the database.

    Raises:
        psycopg2.Error: If there's an error while connecting.
    """
    try:
        connection = psycopg2.connect(**(config or DB_CONFIG))
        return connection
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        raise


def execute_query(query, data=None):
    """
    Execute a query with optional parameters.

    Args:
        query (str): The SQL query to execute.
        data (tuple, optional): Parameters to bind to the query. Defaults to None.

    Returns:
        list: For SELECT queries, returns the fetched results.
        None: For non-SELECT queries (INSERT, UPDATE, DELETE).

    Raises:
        psycopg2.Error: If there's an error while executing the query.
    """
    try:
        # Use a context manager for connection
        with get_connection() as connection:
            with connection.cursor(cursor_factory=RealDictCursor) as cursor:
                if data:
                    cursor.execute(query, data)  # Execute parameterized query
                else:
                    cursor.execute(query)  # Execute query without parameters

                # Return results for SELECT queries
                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()

                # Commit transaction for non-SELECT queries
                connection.commit()
                return None
    except psycopg2.Error as e:
        print(f"Error executing query: {e}")
        raise


def execute_many(query, data_list):
    """
    Execute a query multiple times with different parameters.

    Args:
        query (str): The SQL query to execute.
        data_list (list of tuple): List of parameter tuples to bind to the query.

    Returns:
        None

    Raises:
        psycopg2.Error: If there's an error while executing the query.
    """
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.executemany(query, data_list)
                connection.commit()
    except psycopg2.Error as e:
        print(f"Error executing batch query: {e}")
        raise
