"""
Create tables in the PostgreSQL database.
"""
from psql.connect_db_and_execute_query import execute_query


# SQL query to create the 'employee' table
CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS employee (
    employee_id SERIAL PRIMARY KEY,  -- Auto-incrementing unique ID for each employee
    first_name VARCHAR(25) NOT NULL,  -- Employee's first name, required
    last_name VARCHAR(25) NOT NULL,   -- Employee's last name, required
    age INT CHECK (age > 0),          -- Employee's age, must be greater than 0
    department VARCHAR(15)            -- Department name, optional
);
"""

def create_table():
    """
    Executes the SQL query to create the 'employee' table if it does not exist.
    """
    print("Creating table 'employee'...")
    try:
        execute_query(CREATE_TABLE_QUERY)  # Execute the table creation query
        print("Table 'employee' created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")
        raise  # Re-raise the exception for better debugging

if __name__ == "__main__":
    create_table()
