from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract_data():
    import sys
    sys.path.append(r'D:\biblioteca_projeto\src\extract') #caminho para pasta onde está o scriptc
    import steam_data #importando o script
    steam_data.extract()

def data_transfor():
    import sys
    sys.path.append(r'D:\biblioteca_projeto\src\Transfor\Transfor')
    import data_transfor
    data_transfor.Transfor()
    
def load_to_bigquery():
    import sys
    sys.path.append(r'D:\biblioteca_projeto\src\load')
    import load_to_bigquery
    load_to_bigquery.load()

with DAG(
    'extract_dag',
    default_args={      #informações de configurações da minha dag
        'owner': 'Cibele',
        'depends_on_past': True,
        'start_date': datetime(2024, 11, 17), #data de inicio
        'email': ['cibeledaniel863@gmail.com'],
        'email_on_failure': True,
        'email_on_retry': True
    },
    schedule_interval='@daily', #coloquei ela com a frequencia  diaria 
) as dag:

    start_task = PythonOperator(
        task_id='start',       #criando minha primeira tarefa para iniciar a minha dag
        python_callable=lambda: print('Processo iniciado')
    )

    extract_task = PythonOperator( #classe que utilizei para executar funções python dentro da minhas tarefas 
        task_id='extract_data',   #minha segunda tarefa é extrair os dados do site
        python_callable=extract_data
    )
    
    transfor_task = PythonOperator(
        task_id='transfor_data', # minha terceira tarefa é transformar os dados 
        python_callable=transfor_data
    )

    load_task = PythonOperator(
        task_id='load_to_bigquery', # minha quarta tarefa é subir eles para o big query
        python_callable=load_to_bigquery
    )

    end_task = PythonOperator(
        task_id='end',             #minha quinta tarefa é uma mensagem de processo finalizado
        python_callable=lambda: print('Processo finalizado')
    )

    start_task >> extract_task >> transfor_task >> load_task >> end_task