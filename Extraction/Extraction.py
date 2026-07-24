from dotenv import load_dotenv
import os
load_dotenv()

from pathlib import Path

# folder where THIS script file lives
SCRIPT_DIR = Path(__file__).resolve().parent
# project root is one level up from Extraction/
DATA_DIR = SCRIPT_DIR.parent / "data"

import psycopg2
import pandas as pd

def run_extraction() :

    def convert_binary(value):
        if value is None:
            return value
        else:
            return value.hex()

    try:
        connect = psycopg2.connect(
            host=os.getenv("PG_HOST"),
            database=os.getenv("PG_DATABASE"),
            user=os.getenv("PG_USER"),
            password=os.getenv("PG_PASSWORD")
        )
    except Exception as e:
        print("Error while connecting to PostgreSQL", e)
        raise

    # map each table to its binary column name (if it has one)
    binary_columns = {
        "employees": "photo",
        "categories": "picture"
    }

    tables = ["orders", "order_details", "customers", "employees", "shippers", "suppliers", "products", "categories"]

    for table in tables:
        df = pd.read_sql(f"SELECT * FROM {table}", connect)

        if table in binary_columns:
            col = binary_columns[table]
            df[col] = df[col].apply(convert_binary)

        df.to_csv(DATA_DIR / f"{table}.csv", index=False)
        print(f"Extracted {table}")

if __name__ == "__main__":
    run_extraction()
