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

