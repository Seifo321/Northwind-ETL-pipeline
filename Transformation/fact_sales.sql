CREATE OR REPLACE TABLE fact_sales AS
SELECT order_id, customer_id, employee_id, ship_via AS shipper_id,
        product_id, order_date, unit_price, quantity, discount
FROM NORTHWIND_DW.STAGING_SCH.stg_order_details od
INNER JOIN NORTHWIND_DW.STAGING_SCH.stg_orders o
USING(order_id);

ALTER TABLE fact_sales
    ADD CONSTRAINT pk_fact_sales PRIMARY KEY (order_id, product_id);

ALTER TABLE fact_sales
    ADD CONSTRAINT fk_fact_sales_customers
    FOREIGN KEY (customer_id) REFERENCES dim_customers (customer_id);

ALTER TABLE fact_sales
    ADD CONSTRAINT fk_fact_sales_employees
    FOREIGN KEY (employee_id) REFERENCES dim_employees (employee_id);

ALTER TABLE fact_sales
    ADD CONSTRAINT fk_fact_sales_shippers
    FOREIGN KEY (shipper_id) REFERENCES dim_shippers (shipper_id);

ALTER TABLE fact_sales
    ADD CONSTRAINT fk_fact_sales_products
    FOREIGN KEY (product_id) REFERENCES dim_products (product_id);

ALTER TABLE fact_sales
    ADD CONSTRAINT fk_fact_sales_dates
    FOREIGN KEY (order_date) REFERENCES dim_date (full_date);
