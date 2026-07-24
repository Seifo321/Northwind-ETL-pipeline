from dotenv import load_dotenv
import os

load_dotenv()

import snowflake.connector

from pathlib import Path

# folder where THIS script file lives
SCRIPT_DIR = Path(__file__).resolve().parent
# project root is one level up from Extraction/
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
            csv_path = DATA_DIR / f"{table}.csv"

            if not csv_path.is_file():
                raise FileNotFoundError(f"Missing extracted file: {csv_path}")

            cursor.execute(f"PUT {csv_path.resolve().as_uri()} @northwind_stage OVERWRITE = TRUE")
    except Exception as e:
        print("Error uploading files to Snowflake:", e)
        raise

if __name__ == "__main__" :
    upload_files_to_stage()
