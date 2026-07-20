SELECT DISTINCT f.product_id
FROM fact_sales f
WHERE NOT EXISTS (
    SELECT 1
    FROM dim_products d
    WHERE d.product_id = f.product_id
);
SELECT order_id,product_id,SUM(unit_price*quantity*(1-discount)) AS total_sales
FROM stg_order_details
GROUP BY ALL
ORDER BY order_id , total_sales DESC;