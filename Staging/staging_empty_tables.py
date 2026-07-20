from dotenv import load_dotenv
import os

load_dotenv()

import snowflake.connector

def create_empty_tables():
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

    dic = {
        "orders" : "CREATE TABLE stg_orders (order_id INT, customer_id VARCHAR(5), employee_id INT, order_date DATE, required_date DATE, shipped_date DATE, ship_via INT, freight FLOAT, ship_name VARCHAR(40), ship_address VARCHAR(60), ship_city VARCHAR(15), ship_region VARCHAR(15), ship_postal_code VARCHAR(10), ship_country VARCHAR(15));",
        "order_details" : "CREATE TABLE stg_order_details (order_id INT, product_id INT, unit_price FLOAT, quantity INT, discount FLOAT);",
        "customers" : "CREATE TABLE stg_customers (customer_id VARCHAR(5), company_name VARCHAR(40), contact_name VARCHAR(30), contact_title VARCHAR(30), address VARCHAR(60), city VARCHAR(15), region VARCHAR(15), postal_code VARCHAR(10), country VARCHAR(15), phone VARCHAR(24), fax VARCHAR(24));",
        "employees" : "CREATE TABLE stg_employees (employee_id INT, last_name VARCHAR(20), first_name VARCHAR(10), title VARCHAR(30), title_of_courtesy VARCHAR(25), birth_date DATE, hire_date DATE, address VARCHAR(60), city VARCHAR(15), region VARCHAR(15), postal_code VARCHAR(10), country VARCHAR(15), home_phone VARCHAR(24), extension VARCHAR(4), photo binary, notes TEXT, reports_to INT, photo_path VARCHAR(255));",
        "shippers" : "CREATE TABLE stg_shippers (shipper_id INT, company_name VARCHAR(40), phone VARCHAR(24));",
        "suppliers" : "CREATE TABLE stg_suppliers (supplier_id INT, company_name VARCHAR(40), contact_name VARCHAR(30), contact_title VARCHAR(30), address VARCHAR(60), city VARCHAR(15), region VARCHAR(15), postal_code VARCHAR(10), country VARCHAR(15), phone VARCHAR(24), fax VARCHAR(24), homepage TEXT);",
        "products" : "CREATE TABLE stg_products (product_id INT, product_name VARCHAR(40), supplier_id INT, category_id INT, quantity_per_unit VARCHAR(20), unit_price FLOAT, units_in_stock INT, units_on_order INT, reorder_level INT, discontinued BOOLEAN);",
        "categories" : "CREATE TABLE stg_categories (category_id INT, category_name VARCHAR(15), description varchar, picture binary);"
    }


    for field in dic :
        cursor.execute(dic[field])

if __name__ == "__main__":
    create_empty_tables()