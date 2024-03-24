"""Main database operations."""

import os
from psycopg2 import Error
from psycopg2.extensions import connection

from colors import blue, green, red_error, color_back_end
from config import main_conn

SQL_DIR = "./sql/init"


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
                print(f'{red_error}execution error:{color_back_end}\n{ex}')


if __name__ == '__main__':
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
