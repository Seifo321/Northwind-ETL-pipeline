CREATE OR REPLACE TABLE dim_products AS
SELECT product_id, product_name , category_name, description, supplier_id 
FROM NORTHWIND_DW.STAGING_SCH.stg_products AS p
LEFT JOIN NORTHWIND_DW.STAGING_SCH.STG_CATEGORIES AS c
USING(category_id);

ALTER TABLE dim_products
    ADD CONSTRAINT pk_dim_products PRIMARY KEY (product_id);

ALTER TABLE dim_products
    ADD CONSTRAINT fk_dim_products_suppliers
    FOREIGN KEY (supplier_id) REFERENCES dim_suppliers (supplier_id);
