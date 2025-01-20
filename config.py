import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Database configuration dictionary
DB_CONFIG = {
    'host': os.getenv('POSTGRES_HOST', '172.26.0.2'),       # Default fallback: 'localhost'
    'port': int(os.getenv('POSTGRES_PORT', 5432)),         # Default fallback: 5432
    'user': os.getenv('POSTGRES_USER', 'postgres'),        # Default fallback: 'postgres'
    'password': os.getenv('POSTGRES_PASSWORD', 'admin'),   # Default fallback: 'admin'
    'dbname': os.getenv('POSTGRES_DATABASE', 'default_db') # Default fallback: 'default_db'
}

# Additional configurations
APP_MODE = os.getenv('APP_MODE', 'development')  # For app environment: development/production
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
