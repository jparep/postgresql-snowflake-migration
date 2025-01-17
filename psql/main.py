from create_tables import create_table
from insert_data import insert_initial_data

def main():
    """
    Run the full database setup, including table creation and initial data insertion.
    """
    print("Starting database setup...")
    try:
        create_table()  # Create the 'employee' table
        insert_initial_data()  # Insert initial data
        print("Database setup completed successfully.")
    except Exception as e:
        print(f"An error occurred during the database setup: {e}")

if __name__ == "__main__":
    main()
