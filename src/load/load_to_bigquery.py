import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from pandas_gbq import to_gbq

# Carregue suas credenciais

credencial = service_account.Credentials.from_service_account_file(
    r'D:\\biblioteca_projeto\\meu-primeiro-projet-403011-6924ec2e39ab.json',
    scopes=['https://www.googleapis.com/auth/bigquery']
)
# carregando o arquivo csv
df = pd.read_csv(r"D:\biblioteca_projeto\data_transfor.csv")
df.head()

# Definição do esquema para o BigQuery
table_schema = [
    {"name": "Name", "type": "STRING"},
    {"name": "Discount_percentage", "type": "STRING"},
    {"name": "Price", "type": "STRING"},
    {"name": "Rating", "type": "STRING"},
    {"name": "Release", "type": "STRING"},
    {"name": "Ends", "type": "STRING"},
    {"name": "Started", "type": "STRING"},
]

#print(df.head())

#Envie o DataFrame para o BigQuery
df.to_gbq(destination_table='meu-primeiro-projet-403011.MEUPRIMEIRO.data_transfor', # substitua pelo nome correto da sua tabela nesse steam_sales
          project_id='meu-primeiro-projet-403011',
          if_exists='replace', 
          credentials=credencial,
          table_schema=table_schema)

#replace igual a substituir antiga pela original
#append = adiciona dados no fim da tabela 

