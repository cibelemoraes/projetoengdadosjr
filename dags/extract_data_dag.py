from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract_data():
    import sys
    sys.path.append(r'D:\biblioteca_projeto\src\extract')
    import steam_data
    steam_data.extract()

def load_to_bigquery():
    import sys
    sys.path.append(r'D:\biblioteca_projeto\src\load')
    import load_to_bigquery
    load_to_bigquery.load()

with DAG(
    'extract_dag',
    default_args={
        'owner': 'airflow',
        'depends_on_past': False,
        'start_date': datetime(2024, 11, 17),
        'email': ['seu_email@example.com'],
        'email_on_failure': True,
        'email_on_retry': True
    },
    schedule='@daily,
) as dag:

    start_task = PythonOperator(
        task_id='start',
        python_callable=lambda: print('Processo iniciado')
    )

    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )

    load_task = PythonOperator(
        task_id='load_to_bigquery',
        python_callable=load_to_bigquery
    )

    end_task = PythonOperator(
        task_id='end',
        python_callable=lambda: print('Processo finalizado')
    )

    start_task >> extract_task >> load_task >> end_task