"""
Inserts the first 20 rows into the database.
"""

from .connect_db_and_execute_query import execute_query

# SQL query for inserting data
INSERT_DATA_QUERY = """
INSERT INTO employee (first_name, last_name, age, department)
VALUES (%s, %s, %s, %s);
"""

# Generate initial data
INITIAL_DATA = [
    (f"Employee {i}", f"LastName {i}", 20 + i % 10, "Department A" if i % 2 == 0 else "Department B")
    for i in range(1, 21)
]

def insert_initial_data():
    """
    Inserts the first 20 rows into the 'employee' table.
    """
    print("Inserting initial data into 'employee' table...")
    try:
        for data in INITIAL_DATA:
            execute_query(INSERT_DATA_QUERY, data)  # Pass the query and data tuple
        print("Initial data inserted successfully.")
    except Exception as e:
        print(f"Error inserting initial data: {e}")
        raise  # Re-raise the exception for debugging

if __name__ == "__main__":
    insert_initial_data()
