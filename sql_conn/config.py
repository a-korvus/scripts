"""Database configuration."""

import os

import psycopg2
from dotenv import find_dotenv, load_dotenv
from psycopg2 import OperationalError
from psycopg2.extensions import connection

from colors import color_back_end, red_error

if not find_dotenv(".env"):
    print("No environment specified. Shutdown.")
    exit(1)

load_dotenv(dotenv_path=".env")

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")


def create_conn() -> connection | None:
    """Create a connection to the database."""
    try:
        conn: connection = psycopg2.connect(
            user=db_user,
            password=db_password,
            dbname=db_name,
            host=db_host,
            port=db_port,
        )
    except OperationalError as _e:
        print(
            f"{red_error}Error occurred while "
            f"creating the connection:{color_back_end}\n", _e
        )
    else:
        return conn


def main_conn() -> connection:
    """Use the database connection."""
    conn = create_conn()

    if not conn:
        print("Connection failed.")
        exit(1)

    return conn
