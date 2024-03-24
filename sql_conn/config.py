"""Database configuration."""

import os
from dotenv import find_dotenv, load_dotenv


if not find_dotenv(".env"):
    print("No environment specified. Shutdown.")
    exit(1)

load_dotenv(dotenv_path=".env")

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("POSTGRES_HOST")
db_port = os.getenv("POSTGRES_PORT")
