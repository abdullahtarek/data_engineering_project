from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators import BashOperator

import sys
import os
import pathlib
folder_path = pathlib.Path(__file__).parent.resolve()

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 0,
}

python_env = "/home/dbtEnv"
requirements_file = os.path.join(folder_path,"../dbt_requirements.txt")

with DAG(
    dag_id='number_of_users_dag',
    default_args=default_args,
    description='A DAG to run DBT model number_of_users',
    schedule_interval='*/5 * * * *',  # every 5 minutes
    start_date=datetime(2025, 1, 1),  # change to your desired start date
    catchup=False,
) as dag:

    # Environment setup operator
    setup_environment = BashOperator(
        task_id="setup_environment",
        bash_command=f"""
        if [ -d "{python_env}" ]; then
            echo "Virtual environment already exists at {python_env}, Deleting old env"
            rm -r {python_env}
        fi

        echo "Creating virtual environment at {python_env}"
        python3 -m venv {python_env}

        echo "Installing requirements from {requirements_file}"
        {python_env}/bin/pip install -r {requirements_file}
        """,
        dag=dag,
    )


    task1 = BashOperator(
        task_id='number_of_users',
        python_callable='echo "Hello world" ',
    )

    setup_environment >> task1