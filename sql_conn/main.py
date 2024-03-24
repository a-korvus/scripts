"""Main database operations."""

import os
import psycopg2
import colorama
from colorama import Fore, Back
from psycopg2 import Error, OperationalError
from psycopg2.extensions import connection

from config import db_user, db_password, db_name, db_host, db_port

SQL_DIR = "./sql"

blue = Fore.LIGHTBLUE_EX
green = Fore.LIGHTGREEN_EX
yellow = Fore.LIGHTYELLOW_EX
red_error = Back.LIGHTRED_EX
color_back_end = Back.RESET


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


def main_conn():
    """Use the database connection."""
    conn = create_conn()

    if not conn:
        print("Connection failed.")
        exit(1)

    return conn


def sql_queries(new_conn: connection, sql_file: str) -> None:
    """Execute SQL queries from a file against a database."""
    query_list = []

    with open(sql_file, 'r') as file:
        queries = file.read()

        query_list = queries.split(';')
        if query_list[-1].strip() == '':
            query_list = query_list[:-1]

    for query in query_list:
        query = query.strip()
        if query.startswith('--'):
            print(f'\n{blue}{query}')
            continue

        with new_conn as conn:
            cur = conn.cursor()
            try:
                cur.execute(query)
                conn.commit()
                print(f'{green}executed successfully')
            except Error as ex:
                print(f'{red_error}execution error:\n{ex}')


if __name__ == '__main__':
    colorama.init(autoreset=True)

    with main_conn() as new_conn:
        cursor = new_conn.cursor()
        cursor.execute("SELECT version();")
        print("You're connected to:", cursor.fetchone(), "\n")

    conn: connection = main_conn()
    conn.autocommit = True
    for sql_file in os.listdir(SQL_DIR):
        file_path: str = os.path.join(SQL_DIR, sql_file)
        if os.path.isfile(file_path) and not sql_file.startswith("00_"):
            sql_queries(new_conn=conn, sql_file=file_path)
