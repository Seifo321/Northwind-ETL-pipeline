CREATE OR REPLACE TABLE dim_products AS
SELECT product_id, product_name , category_name, description, supplier_id 
FROM NORTHWIND_DW.STAGING_SCH.stg_products AS p
LEFT JOIN NORTHWIND_DW.STAGING_SCH.STG_CATEGORIES AS c
USING(category_id);