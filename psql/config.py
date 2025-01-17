import os
from dotenv import load_dotenv

"""This file contains the configuration details for connecting to the PostgresSQL database."""

load_dotenv()

DB_CONFIG = {
    'DBNAME': os.getenv('DB_NAME'),
    'USER': os.getenv('USER'),
    'PASSWORD': os.getenv('PASSWORD'),
    'HOST': os.getenv('HOST'),
    'PORT': int(os.getenv('PORT'))
}