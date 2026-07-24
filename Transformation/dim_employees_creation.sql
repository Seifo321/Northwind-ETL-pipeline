CREATE OR REPLACE TABLE dim_employees AS
SELECT employee_id ,CONCAT(first_name, ' ', last_name) AS employee_name , title, hire_date
FROM stg_employees;