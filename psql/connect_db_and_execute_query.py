"""
Create reusable functions for database operations.
"""

import psycopg2
from config import DB_CONFIG

def get_connection():
    """
    Establish and return a connection to the PostgreSQL database.
    
    Returns:
        psycopg2.connection: A connection object to the database.
    
    Raises:
        psycopg2.Error: If there's an error while connecting.
    """
    try:
        connection = psycopg2.connect(**DB_CONFIG)
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
    connection = get_connection()
    cursor = connection.cursor()
    try:
        if data:
            cursor.execute(query, data)  # Execute parameterized query
        else:
            cursor.execute(query)  # Execute query without parameters
        
        # Return results for SELECT queries
        if query.strip().lower().startswith("select"):
            return cursor.fetchall()
        
        # Commit transaction for non-SELECT queries
        connection.commit()
    except psycopg2.Error as e:
        print(f"Error executing query: {e}")
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()
