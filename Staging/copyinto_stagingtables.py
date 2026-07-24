from dotenv import load_dotenv
import os

load_dotenv()

import snowflake.connector

def copy_into_staging_tables():
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
            cursor.execute(f"TRUNCATE TABLE stg_{table}")
            cursor.execute(f"COPY INTO stg_{table} from @northwind_stage/{table}.csv.gz FILE_FORMAT = (TYPE = CSV SKIP_HEADER = 1 , FIELD_OPTIONALLY_ENCLOSED_BY ='\"')")
    except Exception as e:
        print("Error while connecting to Snowflake:", e)
        raise

if __name__ == "__main__" :
    copy_into_staging_tables()
