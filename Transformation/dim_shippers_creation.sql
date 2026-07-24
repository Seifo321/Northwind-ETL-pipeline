CREATE OR REPLACE TABLE dim_shippers AS
SELECT shipper_id, company_name
FROM stg_shippers;