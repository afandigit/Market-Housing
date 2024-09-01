from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

default_args = {

}


def run_scrapy_spider(spider_name):
    # Command to run your Scrapy spider
    import subprocess
    subprocess.run(['scrapy', 'crawl', spider_name])

with DAG(
    'scrapy_market_housing',
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily'
) as dag:
    
    task_run_spider__mubawab_sell = PythonOperator(
        task_id='task_run_spider__mubawab_sell',
        python_callable=run_scrapy_spider,
        op_args=['mubawab_sell'],
    )
