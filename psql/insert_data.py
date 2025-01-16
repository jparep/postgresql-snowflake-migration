"""Inserts first 20 rows into the database"""

from database import execute_query

INSERT_DATA_QUERY = """
INSERT INTO employees (first_name, last_name, age, department
VALUES (%s, %s, %s, %s);
"""

INITIAL_DATA = [
    (f"Employee {i}", 20 + i % 10, "Department A" if i % 2 == 0 else "Department B")
    for i in range(1, 21)
]

def inisert_inital_data():
    """Insert initial data into employees tabel."""
    print("Inserting initial data...")
    for data in INITIAL_DATA:
        execute_query(data)
    print("Initial data inserted successfully.")
