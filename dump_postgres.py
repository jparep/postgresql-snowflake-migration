import os
from dotenv import load_dotenv
import subprocess

# Load environment variables
load_dotenv()

def dump_postgres():
    """Dump PostgreSQL database to a file."""
    dump_file = "data/postgres_backup.sql"
    try:
        # Command to dump PostgreSQL database
        command = [
            "pg_dump",
            "--host", os.getenv("POSTGRES_HOST"),
            "--port", os.getenv("POSTGRES_PORT"),
            "--username", os.getenv("POSTGRES_USER"),
            "--dbname", os.getenv("POSTGRES_DATABASE"),
            "--file", dump_file
        ]

        # Run the command
        subprocess.run(command, check=True, env={"PGPASSWORD": os.getenv("POSTGRES_PASSWORD")})
        print(f"Database dump successful: {dump_file}")
        return dump_file
    except subprocess.CalledProcessError as e:
        print(f"Error during database dump: {e}")
        return None

if __name__ == "__main__":
    dump_postgres()
