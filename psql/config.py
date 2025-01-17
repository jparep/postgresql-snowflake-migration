import os
from dotenv import load_dotenv

"""
This file contains the configuration details for connecting to the PostgreSQL database.
The credentials are loaded from environment variables using the dotenv package.
"""

# Load environment variables from a .env file
load_dotenv()

# Database configuration dictionary
DB_CONFIG = {
    'dbname': os.getenv('DB_NAME', 'default_db'),  # Default value: 'default_db'
    'user': os.getenv('DB_USER', 'postgres'),  # Default value: 'postgres'
    'password': os.getenv('DB_PASSWORD', 'admin'),  # Default value: 'admin'
    'host': os.getenv('DB_HOST', 'localhost'),  # Default value: 'localhost'
    'port': int(os.getenv('DB_PORT', 5432))  # Default value: 5432
}