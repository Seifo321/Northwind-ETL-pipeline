CREATE OR REPLACE TABLE fact_sales AS
SELECT order_id, customer_id, employee_id, ship_via AS shipper_id,
        product_id, order_date, unit_price, quantity, discount
FROM NORTHWIND_DW.STAGING_SCH.stg_order_details od
INNER JOIN NORTHWIND_DW.STAGING_SCH.stg_orders o
USING(order_id);