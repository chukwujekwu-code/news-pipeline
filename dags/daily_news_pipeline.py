import sys
import os
# Get the directory two levels up (project root: ~/airflow-project)
DAGS_FOLDER = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(DAGS_FOLDER)

# Add project root to sys.path
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
    
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scraper.scrape_punch import get_headlines


def print_headlines():
    headlines = get_headlines()
    for headline in headlines:
        print(headline)


default_args = {
    'start_date': datetime(2025, 4, 30)
}


with DAG(
    dag_id='daily_punch_headline_scrapper',
    schedule_interval='@daily',
    default_args=default_args,
    catchup=False,
    tags=['news','scraping']
) as dag:
    
    task_scrape = PythonOperator(
        task_id='scrape_punch_headline',
        python_callable=print_headlines
    )