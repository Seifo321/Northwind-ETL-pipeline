CREATE OR REPLACE TABLE dim_suppliers AS
SELECT supplier_id, company_name, city, region,country
FROM NORTHWIND_DW.STAGING_SCH.stg_suppliers;

ALTER TABLE dim_suppliers MODIFY
    supplier_id SET NOT NULL,
    company_name SET NOT NULL;

ALTER TABLE dim_suppliers
    ADD CONSTRAINT pk_dim_suppliers PRIMARY KEY (supplier_id);
