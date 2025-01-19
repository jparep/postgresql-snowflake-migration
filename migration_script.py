import os
from dotenv import load_dotenv
import psycopg2
import snowflake.connector
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# PostgreSQL connectionb using environment variables
conn_pg = psycopg2.connect(
    host=os.getenv("POSTGRESS_HOST"),
    port=os.getenv("PORTGRESS_PORT"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRESS_PASSWORD"),
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

# Extract data from PostgreSQL
query = "SELECT * FROM employee"
df = pd.read_sql(query, conn_pg)