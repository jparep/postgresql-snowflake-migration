from create_tables import create_table
from insert_data import inisert_inital_data
def main():
    """Run the full database setup."""
    print("Starting database setup...")
    create_table()
    inisert_inital_data()
    print("Database setup completed.")
    
if __name__ == "__main__":
    main()