from prefect import flow, task

from Extraction.Extraction import run_extraction
from Staging.copyinto_stagingtables import copy_into_staging_tables
from Staging.stage_creation import create_stage
from Staging.staging_empty_tables import create_empty_tables
from Staging.staging_files import upload_files_to_stage
from Transformation.transformation import run_transformation
from Validation.validation import run_validation


@task(name="Extract PostgreSQL data", retries=2, retry_delay_seconds=60)
def extract_postgresql_data():
    run_extraction()


@task(name="Create Snowflake stage", retries=2, retry_delay_seconds=60)
def create_snowflake_stage():
    create_stage()


@task(name="Create Snowflake staging tables", retries=2, retry_delay_seconds=60)
def create_snowflake_staging_tables():
    create_empty_tables()


@task(name="Upload CSV files to Snowflake", retries=2, retry_delay_seconds=60)
def upload_csv_files():
    upload_files_to_stage()


@task(name="Load Snowflake staging tables", retries=2, retry_delay_seconds=60)
def load_snowflake_staging_tables():
    copy_into_staging_tables()


@task(name="Build warehouse dimensions and fact table", retries=2, retry_delay_seconds=60)
def build_warehouse_models():
    run_transformation()


@task(name="Validate warehouse data", retries=2, retry_delay_seconds=60)
def validate_warehouse_data():
    run_validation()


@flow(name="northwind-etl", log_prints=True)
def northwind_etl():
    extract_postgresql_data()
    create_snowflake_stage()
    create_snowflake_staging_tables()
    upload_csv_files()
    load_snowflake_staging_tables()
    build_warehouse_models()
    validate_warehouse_data()


if __name__ == "__main__":
    northwind_etl()
