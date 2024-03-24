"""Some select queries."""

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from psycopg2.extensions import connection, cursor

from config import main_conn

SQL_DIR = "./sql/select"

query = """
SELECT "name", "price" FROM good;
"""

new_conn: connection = main_conn()

with new_conn as conn:
    cur: cursor = conn.cursor()
    cur.execute(query)
    result: list = cur.fetchall()

workbook: Workbook = Workbook()
sheet: Worksheet = workbook.active
sheet.append(("name", "price"))

for elem in result:
    sheet.append(elem)

workbook.save("example.xlsx")
