SELECT
    (SELECT COUNT(*) FROM stg_order_details) AS staging_row_count,
    (SELECT COUNT(*) FROM fact_sales) AS fact_row_count;

SELECT 'customer_id' AS relationship, COUNT(*) AS orphan_rows
FROM fact_sales f
WHERE f.customer_id IS NOT NULL
  AND NOT EXISTS (SELECT 1 FROM dim_customers d WHERE d.customer_id = f.customer_id)
UNION ALL
SELECT 'employee_id', COUNT(*)
FROM fact_sales f
WHERE f.employee_id IS NOT NULL
  AND NOT EXISTS (SELECT 1 FROM dim_employees d WHERE d.employee_id = f.employee_id)
UNION ALL
SELECT 'shipper_id', COUNT(*)
FROM fact_sales f
WHERE f.shipper_id IS NOT NULL
  AND NOT EXISTS (SELECT 1 FROM dim_shippers d WHERE d.shipper_id = f.shipper_id)
UNION ALL
SELECT 'product_id', COUNT(*)
FROM fact_sales f
WHERE f.product_id IS NOT NULL
  AND NOT EXISTS (SELECT 1 FROM dim_products d WHERE d.product_id = f.product_id)
UNION ALL
SELECT 'order_date', COUNT(*)
FROM fact_sales f
WHERE f.order_date IS NOT NULL
  AND NOT EXISTS (SELECT 1 FROM dim_date d WHERE d.full_date = f.order_date);

SELECT
    ROUND(COALESCE((SELECT SUM(unit_price * quantity * (1 - discount)) FROM stg_order_details), 0), 2) AS staging_sales_total,
    ROUND(COALESCE((SELECT SUM(unit_price * quantity * (1 - discount)) FROM fact_sales), 0), 2) AS fact_sales_total;
