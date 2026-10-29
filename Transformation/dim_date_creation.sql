CREATE
OR REPLACE TABLE dim_date AS
SELECT
    DATEADD(day, n, '1996-01-01') AS full_date,
    YEAR(DATEADD(day, n, '1996-01-01')) AS year,
    MONTH(DATEADD(day, n, '1996-01-01')) AS month,
    DAY(DATEADD(day, n, '1996-01-01')) AS day,
    TO_CHAR(DATEADD(day, n, '1996-01-01'), 'MMMM') AS month_name,
    DAYNAME(DATEADD(day, n, '1996-01-01')) AS day_name,
    CASE
        WHEN DAYOFWEEK(DATEADD(day, n, '1996-01-01')) IN (0, 6) THEN TRUE
        ELSE FALSE
    END AS is_weekend,
    QUARTER(DATEADD(day, n, '1996-01-01')) AS quarter
FROM
    (
        SELECT
            SEQ4() AS n
        FROM
            TABLE(GENERATOR(ROWCOUNT => 1096))
    );

ALTER TABLE dim_date MODIFY
    full_date SET NOT NULL,
    year SET NOT NULL,
    month SET NOT NULL,
    day SET NOT NULL,
    month_name SET NOT NULL,
    day_name SET NOT NULL,
    is_weekend SET NOT NULL,
    quarter SET NOT NULL;

ALTER TABLE dim_date
    ADD CONSTRAINT pk_dim_date PRIMARY KEY (full_date);
