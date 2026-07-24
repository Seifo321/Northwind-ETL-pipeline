# Northwind ETL Pipeline

This project extracts Northwind data from PostgreSQL, loads it into Snowflake, builds warehouse models, and validates the result.

## Setup

1. Create and activate a virtual environment.
2. Install dependencies with `python -m pip install -r requirements.txt`.
3. Copy `.env.example` to `.env` and provide the PostgreSQL and Snowflake credentials.

## Run the pipeline

Run the Prefect flow with:

```powershell
python orch.py
```

The flow runs these steps in order:

1. Extract PostgreSQL tables to `data/*.csv`.
2. Create the Snowflake stage and staging tables if needed.
3. Upload the CSV files to the Snowflake stage.
4. Refresh the staging tables from the uploaded files.
5. Build dimension and fact tables.
6. Validate product keys and sales totals.

Each task retries twice after a failure. A failed task stops later tasks from running.
