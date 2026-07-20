from dotenv import load_dotenv
import os

load_dotenv()

import snowflake.connector

from pathlib import Path

# folder where THIS script file lives
SCRIPT_DIR = Path(__file__).resolve().parent
# project root is one level up from Staging/
DATA_DIR = SCRIPT_DIR.parent / "data"

def upload_files_to_stage():
    try:
        conn = snowflake.connector.connect(
            account=os.getenv("SNOWFLAKE_ACCOUNT"),
            user=os.getenv("SNOWFLAKE_USER"),
            password=os.getenv("SNOWFLAKE_PASSWORD"),
            warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
            database=os.getenv("SNOWFLAKE_DATABASE"),
            schema=os.getenv("SNOWFLAKE_SCHEMA")
        )
        cursor=  conn.cursor()
        cursor.execute("SELECT CURRENT_VERSION();")
        result = cursor.fetchone()
        print("Connected successfully! Snowflake version:", result[0])

        tables = ["orders", "order_details", "customers", "employees", "shippers", "suppliers", "products", "categories"]
        for table in tables:
            file_path = (DATA_DIR / f"{table}.csv").as_posix()
            cursor.execute(f"PUT file://{file_path} @northwind_stage OVERWRITE = TRUE")
    except Exception as e:
        print("Error while connecting to Snowflake:", e)

if __name__ == "__main__" :
    upload_files_to_stage()