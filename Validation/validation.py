from dotenv import load_dotenv
import os

load_dotenv()

import snowflake.connector


from pathlib import Path

def run_validation():
    try:
            conn = snowflake.connector.connect(
                account=os.getenv("SNOWFLAKE_ACCOUNT"),
                user=os.getenv("SNOWFLAKE_USER"),
                password=os.getenv("SNOWFLAKE_PASSWORD"),
                warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
                database=os.getenv("SNOWFLAKE_DATABASE"),
                schema=os.getenv("SNOWFLAKE_SCHEMA")
            )
            cursor = conn.cursor()
            cursor.execute("SELECT CURRENT_VERSION();")
            result = cursor.fetchone()
            print("Connected successfully! Snowflake version:", result[0])
    except Exception as e:
            print("Error while connecting to Snowflake:", e)
            raise

    SCRIPT_DIR = Path(__file__).resolve().parent
    sql_file_path = SCRIPT_DIR / "validation.sql"

    with open(sql_file_path, "r") as f:
        sql_content = f.read()

        results = []
        for cur in conn.execute_string(sql_content):
            results.append(cur.fetchall())

    orphan_product_rows, sales_totals = results
    print(f"Orphan product rows: {orphan_product_rows}")
    print(f"Sales totals (staging, fact): {sales_totals[0]}")

    if orphan_product_rows:
        raise ValueError("Validation failed: fact_sales contains product IDs missing from dim_products.")

    staging_sales_total, fact_sales_total = sales_totals[0]
    if staging_sales_total != fact_sales_total:
        raise ValueError("Validation failed: staging and fact_sales totals do not match.")

if __name__ == "__main__" :
    run_validation()
