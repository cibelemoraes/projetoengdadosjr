import pandas as pd
import datetime
import re

#carregando o arquivo CSV
df = pd.read_csv('D:\\biblioteca_projeto\\steam_sales.csv')


#Removendo Linhas Vazias
df = df.dropna(subset=['Name', 'Release'])


#funcao para converter datas
def converte_datas(data):
    meses = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04', 'May': '05', 'Jun': '06', 
             'Jul': '07', 'Aug': '08', 'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}
    
    if pd.isna(data) or len(data.split()) != 2:  # Verifica se é nulo, se não ele executa meu if
        return None
    mes, ano = data.split()
    return f"{meses[mes]}/{ano}"

#aplica a função de para converte coluna Relese
df['Release'] = df['Release'].apply(converte_datas)

#criando uma coluna para os jogos gratis 
df['Jogos Gratis'] = df['Price'].apply(lambda x: 'free' if x== 'R$ 0,00' else '')

#print(df['Release'].head())
print(df)

# Salvando o DataFrame modificado
df.to_csv('D:\\biblioteca_projeto\\data_transfor.csv', index=False)
    







