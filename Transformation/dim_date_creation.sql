CREATE TABLE IF NOT EXISTS dim_date (
    full_date DATE,
    year NUMBER(4, 0) NOT NULL,
    month NUMBER(2, 0) NOT NULL,
    day NUMBER(2, 0) NOT NULL,
    month_name VARCHAR NOT NULL,
    day_name VARCHAR NOT NULL,
    is_weekend BOOLEAN NOT NULL,
    quarter NUMBER(2, 0) NOT NULL,
    CONSTRAINT pk_dim_date PRIMARY KEY (full_date)
);

TRUNCATE TABLE dim_date;

INSERT INTO dim_date (
    full_date,
    year,
    month,
    day,
    month_name,
    day_name,
    is_weekend,
    quarter
)
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
FROM (
    SELECT SEQ4() AS n
    FROM TABLE(GENERATOR(ROWCOUNT => 1096))
);
