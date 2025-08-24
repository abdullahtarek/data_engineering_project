from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def hello_world():
    print("Hello World")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 0,
}

with DAG(
    dag_id='hello_world_dag',
    default_args=default_args,
    description='A simple DAG that prints Hello World every 5 minutes',
    schedule_interval='*/5 * * * *',  # every 5 minutes
    start_date=datetime(2025, 1, 1),  # change to your desired start date
    catchup=False,
    tags=['example'],
) as dag:

    task1 = PythonOperator(
        task_id='print_hello',
        python_callable=hello_world,
    )

    task1