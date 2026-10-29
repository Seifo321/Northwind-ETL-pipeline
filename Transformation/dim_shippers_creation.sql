CREATE OR REPLACE TABLE dim_shippers AS
SELECT shipper_id, company_name
FROM NORTHWIND_DW.STAGING_SCH.stg_shippers;

ALTER TABLE dim_shippers MODIFY
    shipper_id SET NOT NULL,
    company_name SET NOT NULL;

ALTER TABLE dim_shippers
    ADD CONSTRAINT pk_dim_shippers PRIMARY KEY (shipper_id);
