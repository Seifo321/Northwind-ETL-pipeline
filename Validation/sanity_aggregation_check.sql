SELECT order_id,product_id,SUM(unit_price*quantity*(1-discount)) AS total_sales 
FROM stg_order_details
GROUP BY ALL 
ORDER BY order_id , total_sales DESC;