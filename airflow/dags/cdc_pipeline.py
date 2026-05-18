from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
'cdc_pipeline',
start_date=datetime(2025,1,1),
schedule='@daily',
catchup=False
) as dag:

    check_kafka=BashOperator(
    task_id='check_kafka',
    bash_command='docker ps'
    )

    consumer=BashOperator(
    task_id='run_consumer',
    bash_command='spark-submit spark/consumer.py'
    )

    validate=BashOperator(
    task_id='validate_output',
    bash_command='ls data/bronze'
    )

check_kafka>>consumer>>validate
