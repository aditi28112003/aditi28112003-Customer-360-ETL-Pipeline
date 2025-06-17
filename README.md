# aditi28112003-Customer-360-ETL-Pipeline
This project demonstrates the development of a complete data pipeline to generate a 360° view of customer data by integrating and transforming data from multiple sources. It also includes a basic churn prediction use case using derived features.
 Features

     Extracted transactional and profile data from CSV files

     Cleaned and merged data using pandas, handling missing values and inconsistencies

     Engineered features like total_spend to enrich the customer profile

     Automated ETL pipeline using Apache Airflow

     Prepared data for downstream ML tasks like churn prediction

Tech Stack

    Python, Pandas, NumPy

    SQL (simulated through dataframes)

    Apache Airflow (for DAG-based automation)

    AWS S3 (simulated local storage)

Folder Structure

Customer_360_Data_Pipeline/
├── data/
│   ├── transactions.csv
│   └── profiles.csv
├── scripts/
│   └── etl.py
├── dags/
│   └── airflow_etl_dag.py
└── README.md

Future Improvements

    Integrate actual cloud storage (e.g., AWS S3)

    Add churn model training script (Logistic Regression, XGBoost, etc.)

    Connect to real-time data sources or APIs
