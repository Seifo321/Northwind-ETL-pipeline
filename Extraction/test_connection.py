from dotenv import load_dotenv
import os

load_dotenv()

import psycopg2
try :
    connect = psycopg2.connect(
        host=os.getenv("PG_HOST"),
        database=os.getenv("PG_DATABASE"),
        user=os.getenv("PG_USER"),
        password=os.getenv("PG_PASSWORD")
    )
    cursor = connect.cursor()
    cursor.execute("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'categories' ")
    rows = cursor.fetchall()
    # print(rows)
    for row in rows:
        print(row)
except Exception as e:
    print("Error while connecting to PostgreSQL", e)
