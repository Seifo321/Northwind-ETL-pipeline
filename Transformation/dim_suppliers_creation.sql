CREATE OR REPLACE TABLE dim_suppliers AS
SELECT supplier_id, company_name, city, region,country
FROM stg_suppliers;