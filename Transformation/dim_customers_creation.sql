CREATE OR REPLACE TABLE dim_customers AS 
SELECT customer_id , company_name, city, region ,country
FROM stg_customers;
-- DROP TABLE dim_customers;
