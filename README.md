# PostgreSQL to Snowflake Migration

This project involves developing a PostgreSQL database with tables for employees, customers, departments, and sales. The data will then be migrated to a Snowflake data warehouse using dbt (data build tool).

## Table of Contents
- [Project Overview](#project-overview)
- [Database Schema](#database-schema)
- [Setting Up PostgreSQL](#setting-up-postgresql)
- [Migrating to Snowflake](#migrating-to-snowflake)
- [Using dbt](#using-dbt)
- [Contributing](#contributing)
- [License](#license)

## Project Overview
The goal of this project is to create a PostgreSQL database with the following tables:
- Employees
- Customers
- Departments
- Sales

After the database is set up, the data will be migrated to a Snowflake data warehouse using dbt.

## Database Schema
### Employees Table
- `employee_id` (Primary Key)
- `first_name`
- `last_name`
- `email`
- `phone_number`
- `hire_date`
- `job_id`
- `salary`
- `manager_id`
- `department_id`

### Customers Table
- `customer_id` (Primary Key)
- `first_name`
- `last_name`
- `email`
- `phone_number`
- `address`
- `city`
- `state`
- `zip_code`

### Departments Table
- `department_id` (Primary Key)
- `department_name`
- `manager_id`
- `location_id`

### Sales Table
- `sale_id` (Primary Key)
- `product_id`
- `customer_id`
- `sale_date`
- `amount`

## Setting Up PostgreSQL
1. Install PostgreSQL on your machine.
2. Create a new database.
3. Create the tables using the schema provided above.
4. Insert sample data into the tables.

## Migrating to Snowflake
1. Set up a Snowflake account.
2. Create a new Snowflake database.
3. Create the corresponding tables in Snowflake.
4. Use dbt to extract data from PostgreSQL and load it into Snowflake.

## Using dbt
1. Install dbt on your machine.
2. Configure dbt to connect to both PostgreSQL and Snowflake.
3. Create dbt models to transform and load data from PostgreSQL to Snowflake.
4. Run dbt commands to execute the migration.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.