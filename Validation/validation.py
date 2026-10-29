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

    staging_row_count, fact_row_count = results[0][0]
    orphan_relationships = results[1]
    sales_totals = results[2][0]

    print(f"Row counts (staging order_details, fact_sales): {staging_row_count}, {fact_row_count}")
    print(f"Orphan rows by relationship: {orphan_relationships}")
    print(f"Sales totals (staging, fact): {sales_totals}")

    if staging_row_count != fact_row_count:
        raise ValueError(
            f"Validation failed: stg_order_details has {staging_row_count} rows, "
            f"but fact_sales has {fact_row_count}."
        )

    orphaned = [(relationship, count) for relationship, count in orphan_relationships if count]
    if orphaned:
        raise ValueError(f"Validation failed: fact_sales has unresolved dimension references: {orphaned}")

    staging_sales_total, fact_sales_total = sales_totals
    if staging_sales_total != fact_sales_total:
        raise ValueError("Validation failed: staging and fact_sales totals do not match.")

if __name__ == "__main__" :
    run_validation()
