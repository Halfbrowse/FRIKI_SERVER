import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()
external_db_url = os.getenv("EXTERNAL_DB_URL")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")


def connect_to_database():
    # Load environment variables from .env file
    external_db_url = os.getenv("EXTERNAL_DB_URL")
    conn = psycopg2.connect(
        f"postgres://{db_user}:{db_password}@{external_db_url}/friki_db"
    )
    c = conn.cursor()

    # Return the connection object
    return conn
