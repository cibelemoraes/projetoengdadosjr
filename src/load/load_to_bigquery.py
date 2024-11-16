import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from pandas_gbq import to_gbq

# Carregue suas credenciais

credencial = service_account.Credentials.from_service_account_file(
    r'D:\biblioteca_projeto\meu-primeiro-projet-403011-f594f7373847.json',
    scopes=['https://oauth2.googleapis.com/token']
)
# carregando o arquivo csv
df = pd.read_csv(r"D:\biblioteca_projeto\steam_sales.csv")
df.head()
#print(df.head())
