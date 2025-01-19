import psycopg2
import snowflake.connector
import pandas as pd

# PostgreSQL connection
pg_conn = psycopg2.connect(
    host="postgres",
    port=5432,
    user="postgres123",
    password="admin",
    database="test_db"
)

# Snowflake connection
sf_conn = snowflake.connector.connect(
    user="your_snowflake_user",
    password="your_snowflake_password",
    account="your_snowflake_account",
    database="test_db_snowflake",
    schema="public"
)

# Extract data from PostgreSQL
query = "SELECT * FROM your_table"
df = pd.read_sql(query, pg_conn)

# Load data into Snowflake
cursor = sf_conn.cursor()
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO your_table VALUES (%s, %s, %s)",
        tuple(row)
    )

pg_conn.close()
sf_conn.close()
