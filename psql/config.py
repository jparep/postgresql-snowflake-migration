import os

"""This file contains the configuration details for connecting to the PostgresSQL database."""

DB_CONFIG = {
    'DBNAME': os.getenv('DB_NAME'),
    'USER': os.getenv('USER'),
    'PASSWORD': os.getenv('PASSWORD'),
    'HOST': os.getenv('HOST'),
    'PORT': os.getenv('PORT')
}