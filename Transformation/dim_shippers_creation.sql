CREATE TABLE IF NOT EXISTS dim_shippers (
    shipper_id INT,
    company_name VARCHAR(40) NOT NULL,
    CONSTRAINT pk_dim_shippers PRIMARY KEY (shipper_id)
);

TRUNCATE TABLE dim_shippers;

INSERT INTO dim_shippers (shipper_id, company_name)
SELECT
    shipper_id,
    company_name
FROM NORTHWIND_DW.STAGING_SCH.stg_shippers;
