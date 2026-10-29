CREATE
OR REPLACE TABLE dim_customers AS
SELECT
    customer_id,
    company_name,
    city,
    region,
    country
FROM
    NORTHWIND_DW.STAGING_SCH.stg_customers;

ALTER TABLE dim_customers
    ADD CONSTRAINT pk_dim_customers PRIMARY KEY (customer_id);

