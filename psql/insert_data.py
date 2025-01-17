"""
Inserts the first 20 rows into the database.
"""

from database import execute_query

# SQL query for inserting data
INSERT_DATA_QUERY = """
INSERT INTO employees (first_name, last_name, age, department)
VALUES (%s, %s, %s, %s);
"""

# Generate initial data
INITIAL_DATA = [
    (f"Employee {i}", f"LastName {i}", 20 + i % 10, "Department A" if i % 2 == 0 else "Department B")
    for i in range(1, 21)
]

def insert_initial_data():
    """Insert initial data into employees table."""
    print("Inserting initial data...")
    for data in INITIAL_DATA:
        execute_query(INSERT_DATA_QUERY, data)  # Pass the query and data tuple
    print("Initial data inserted successfully.")

if __name__ == "__main__":
    insert_initial_data()
