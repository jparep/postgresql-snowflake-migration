import os
from dotenv import load_dotenv
import psycopg2
import snowflake.connector
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# PostgreSQL connection using environment variables
conn_pg = psycopg2.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    database=os.getenv("POSTGRES_DATABASE")
)

# Snowflake Connection using environment variables
conn_sf = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

try:
    # Extract data from PostgreSQL
    query = "SELECT * FROM employee"
    df = pd.read_sql(query, conn_pg)

    # Load data into Snowflake
    cursor = conn_sf.cursor()
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO employee VALUES (%s, %s, %s, %s)",
            tuple(row)
        )
    print("Data migration completed successfully.")
finally:
    # Close connections
    conn_pg.close()
    conn_sf.close()
