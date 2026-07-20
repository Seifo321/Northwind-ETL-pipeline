CREATE OR REPLACE TABLE fact_sales AS
SELECT order_id, customer_id, employee_id, ship_via AS shipper_id,
        product_id, order_date, unit_price, quantity, discount
FROM stg_order_details od
INNER JOIN stg_orders o
USING(order_id);
-- TRUNCATE TABLE fact_sales;
