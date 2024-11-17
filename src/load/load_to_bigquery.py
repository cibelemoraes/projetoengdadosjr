import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from pandas_gbq import to_gbq

# Carregue suas credenciais

credencial = service_account.Credentials.from_service_account_file(
    r'D:\\biblioteca_projeto\\meu-primeiro-projet-403011-c7fe55c69300.json',
    scopes=['https://www.googleapis.com/auth/bigquery']
)
# carregando o arquivo csv
df = pd.read_csv(r"D:\biblioteca_projeto\data_transfor.csv")
df.head()
#print(df.head())

#Envie o DataFrame para o BigQuery
df.to_gbq(destination_table='meu-primeiro-projet-403011.MEUPRIMEIRO.steam_sales', # substitua pelo nome correto da sua tabela nesse steam_sales
          project_id='meu-primeiro-projet-403011',
          if_exists='replace', 
          credentials=credencial)

#replace igual a substituir antiga pela original
#append = adiciona dados no fim da tabela 

