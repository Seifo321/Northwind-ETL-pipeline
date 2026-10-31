CREATE TABLE IF NOT EXISTS dim_customers (
    customer_id VARCHAR(5),
    company_name VARCHAR(40) NOT NULL,
    city VARCHAR(15),
    region VARCHAR(15),
    country VARCHAR(15),
    CONSTRAINT pk_dim_customers PRIMARY KEY (customer_id)
);

TRUNCATE TABLE dim_customers;

INSERT INTO dim_customers (customer_id, company_name, city, region, country)
SELECT
    customer_id,
    company_name,
    city,
    region,
    country
FROM NORTHWIND_DW.STAGING_SCH.stg_customers;
