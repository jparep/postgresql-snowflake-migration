"""Create tables in the PostgreSQL database."""

from database import excute_query

CREATE_TABLE_QUERY = """
CREATE TABLE IF NOT EXISTS empoyee (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(30),
    last_name VARCHAR(30),
    age INT
);
"""