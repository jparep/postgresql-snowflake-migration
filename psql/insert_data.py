"""Inserts first 20 rows into the database"""

from database import execute_query

INSERT_DATA_QUERY = """
INSERT INTO employees (first_name, last_name, age)
VALUES (%s, %s, %s)
"""