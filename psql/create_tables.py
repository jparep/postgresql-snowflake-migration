"""Create tables in the PostgreSQL database."""

from database import execute_query

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS empoyee (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(25),
    last_name VARCHAR(25),
    age INT,
    department VARCHAR (15)
);
"""
def create_table():
    """Run the table creation query."""
    print("Creating table...")
    execute_query(CREATE_TABLE_QUERY)
