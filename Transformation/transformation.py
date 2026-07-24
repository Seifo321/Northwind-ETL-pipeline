from dotenv import load_dotenv
import os

load_dotenv()

import snowflake.connector


from pathlib import Path


def run_transformation():

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




    # folder where THIS script file lives
    SCRIPT_DIR = Path(__file__).resolve().parent


    sql_files = ["dim_customers_creation.sql", "dim_products_creation.sql",
                "dim_employees_creation.sql", "dim_suppliers_creation.sql",
                "dim_shippers_creation.sql", "dim_date_creation.sql", "fact_sales.sql"]



    #  loop through the list of SQL files and execute each one
    for sql_file in (sql_files):
        sql_file_path = SCRIPT_DIR / sql_file
        with open(sql_file_path, "r") as f:
            sql_content = f.read()

            for cur in conn.execute_string(sql_content):
                cur.fetchall()

if __name__ == "__main__":
    run_transformation()
