CREATE TABLE IF NOT EXISTS dim_suppliers (
    supplier_id INT,
    company_name VARCHAR(40) NOT NULL,
    city VARCHAR(15),
    region VARCHAR(15),
    country VARCHAR(15),
    CONSTRAINT pk_dim_suppliers PRIMARY KEY (supplier_id)
);

TRUNCATE TABLE dim_suppliers;

INSERT INTO dim_suppliers (supplier_id, company_name, city, region, country)
SELECT
    supplier_id,
    company_name,
    city,
    region,
    country
FROM NORTHWIND_DW.STAGING_SCH.stg_suppliers;
