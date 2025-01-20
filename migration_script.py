import os
from dotenv import load_dotenv
import psycopg2
import snowflake.connector
import pandas as pd

# Load environment variables
load_dotenv()

# PostgreSQL connection
try:
    conn_pg = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "localhost"),
        port=os.getenv("POSTGRES_PORT", "5432"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        database=os.getenv("POSTGRES_DATABASE")
    )
    print("Connected to PostgreSQL.")
except Exception as e:
    print(f"Error connecting to PostgreSQL: {e}")
    exit(1)

# Snowflake connection
try:
    conn_sf = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )
    print("Connected to Snowflake.")
except Exception as e:
    print(f"Error connecting to Snowflake: {e}")
    conn_pg.close()
    exit(1)

try:
    # Extract data from PostgreSQL
    query = "SELECT * FROM employee"
    df = pd.read_sql(query, conn_pg)
    print(f"Fetched {len(df)} rows from PostgreSQL.")

    # Validate DataFrame
    if df.empty:
        print("No data found in PostgreSQL table.")
        exit(0)

    # Create a CSV file for bulk upload
    temp_file = "/tmp/employee_data.csv"
    df.to_csv(temp_file, index=False)
    print(f"Data written to {temp_file} for Snowflake upload.")

    # Load data into Snowflake using bulk upload
    cursor = conn_sf.cursor()
    cursor.execute(f"PUT file://{temp_file} @%employee")
    cursor.execute("COPY INTO employee FROM @%employee FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1)")
    print("Data migration to Snowflake completed successfully.")
except Exception as e:
    print(f"Error during data migration: {e}")
finally:
    # Close connections
    conn_pg.close()
    conn_sf.close()
    print("Connections closed.")
