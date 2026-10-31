CREATE TABLE IF NOT EXISTS dim_employees (
    employee_id INT,
    employee_name VARCHAR(31) NOT NULL,
    title VARCHAR(30),
    hire_date DATE,
    CONSTRAINT pk_dim_employees PRIMARY KEY (employee_id)
);

TRUNCATE TABLE dim_employees;

INSERT INTO dim_employees (employee_id, employee_name, title, hire_date)
SELECT
    employee_id,
    CONCAT(first_name, ' ', last_name) AS employee_name,
    title,
    hire_date
FROM NORTHWIND_DW.STAGING_SCH.stg_employees;
