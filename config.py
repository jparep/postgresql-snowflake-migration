import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Database configuration dictionary
DB_CONFIG = {
    'host': os.getenv('POSTGRES_HOST', 'postgres'),
    'port': int(os.getenv('POSTGRES_PORT', 5432)),  # Use 5432 for internal Docker communication
    'user': os.getenv('POSTGRES_USER', 'postgres123'),
    'password': os.getenv('POSTGRES_PASSWORD', 'admin'),
    'dbname': os.getenv('POSTGRES_DATABASE', 'test_db')
}

# Additional configurations
APP_MODE = os.getenv('APP_MODE', 'development')  # For app environment: development/production
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
