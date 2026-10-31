CREATE TABLE IF NOT EXISTS dim_products (
    product_id INT,
    product_name VARCHAR(40) NOT NULL,
    category_name VARCHAR(15),
    description VARCHAR,
    supplier_id INT NOT NULL,
    CONSTRAINT pk_dim_products PRIMARY KEY (product_id),
    CONSTRAINT fk_dim_products_suppliers
        FOREIGN KEY (supplier_id) REFERENCES dim_suppliers (supplier_id)
);

TRUNCATE TABLE dim_products;

INSERT INTO dim_products (product_id, product_name, category_name, description, supplier_id)
SELECT
    product_id,
    product_name,
    category_name,
    description,
    supplier_id
FROM NORTHWIND_DW.STAGING_SCH.stg_products AS p
LEFT JOIN NORTHWIND_DW.STAGING_SCH.STG_CATEGORIES AS c
USING (category_id);
