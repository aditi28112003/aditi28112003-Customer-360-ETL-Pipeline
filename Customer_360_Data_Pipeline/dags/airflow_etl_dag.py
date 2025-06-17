from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(dag_id="customer_360_etl", start_date=datetime(2024, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    run_etl = BashOperator(
        task_id="run_etl_script",
        bash_command="python /path/to/scripts/etl.py"
    )
