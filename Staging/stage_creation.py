from dotenv import load_dotenv
import os

load_dotenv()

import snowflake.connector

def create_stage():
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


    cursor.execute("CREATE STAGE IF NOT EXISTS northwind_stage;")

if __name__ == "__main__":
    create_stage()
