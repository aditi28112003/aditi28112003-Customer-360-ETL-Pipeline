# Customer 360 Data Pipeline

This project builds an end-to-end data pipeline that consolidates multi-source customer data to generate a unified Customer 360 view.

## Features
- Extract and clean transactional and profile data using Pandas & SQL
- Schedule ETL using Apache Airflow
- Store cleaned data in AWS S3 (simulated here)
- Perform churn prediction on unified dataset

## Stack
Python, Pandas, SQL, Airflow, AWS S3

Run the ETL: `python scripts/etl.py`
