SELECT DISTINCT f.product_id
FROM fact_sales f
WHERE NOT EXISTS (
    SELECT 1
    FROM dim_products d
    WHERE d.product_id = f.product_id
);
SELECT
    ROUND(COALESCE((SELECT SUM(unit_price * quantity * (1 - discount)) FROM stg_order_details), 0), 2) AS staging_sales_total,
    ROUND(COALESCE((SELECT SUM(unit_price * quantity * (1 - discount)) FROM fact_sales), 0), 2) AS fact_sales_total;
