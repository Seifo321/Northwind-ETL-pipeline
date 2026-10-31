CREATE OR REPLACE TABLE dim_employees AS
SELECT employee_id ,CONCAT(first_name, ' ', last_name) AS employee_name , title, hire_date
FROM NORTHWIND_DW.STAGING_SCH.stg_employees;

ALTER TABLE dim_employees MODIFY
    employee_name SET NOT NULL;

ALTER TABLE dim_employees
    ADD CONSTRAINT pk_dim_employees PRIMARY KEY (employee_id);
