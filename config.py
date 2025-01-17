import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Database configuration dictionary
DB_CONFIG = {
    'dbname': os.getenv('DB_NAME', 'default_db'),
    'user': os.getenv('DB_USER', 'postgres'),
    'password': os.getenv('DB_PASSWORD', 'admin'),
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 5432)),
}
