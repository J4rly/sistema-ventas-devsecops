import os
import psycopg

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres123@localhost:5432/fran_db"
)

def get_connection():
    return psycopg.connect(DATABASE_URL)
