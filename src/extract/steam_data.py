import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import logging
import time

# Configuração do logging
logging.basicConfig(level=logging.INFO)

# Caminho para o geckodriver
geckodriver_path = r'D:\\biblioteca_projeto\\geckodriver.exe'

# Inicializando o WebDriver
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service)

# Acessando o site
url = 'https://steamdb.info/sales/'
driver.get(url)

# Lista para armazenar os dados de todas as páginas
games = []

# Loop para navegar entre as páginas (1 a 20)
for page in range(1, 21):
    # Aguarda a tabela carregar
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "DataTables_Table_0"))
    )

    # Extrai o conteúdo da página atual
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extraindo os dados da tabela
    table = soup.find(id="DataTables_Table_0")
    rows = table.find_all("tr", class_="app") #extraindo os dados de todas as tags tr e casses app
    
    for row in rows:
        data_cells = row.find_all("td")
        games.append({                       #adicionando os dados a lista games
            "Name": data_cells[2].find("a").text.strip(),
            "Discount_percentage": data_cells[3].text.strip(),
            "Price": data_cells[4].text.strip(),
            "Rating": data_cells[5].text.strip(),
            "Release": data_cells[6].text.strip(),
            "Ends": data_cells[7].text.strip(),
            "Started": data_cells[8].text.strip()
        })
    
    logging.info(f"Dados extraídos da página {page} com sucesso.")
    
    # Tenta clicar no botão da próxima página, exceto na última
    if page < 20:
        next_button = driver.find_element(By.CSS_SELECTOR, "button.dt-paging-button.next")
        next_button.click()
        time.sleep(2)  # Pequenos intervalo para a página carregar

# Fechando o driver
driver.quit()

# Criando o DataFrame
df = pd.DataFrame(games)
logging.info("DataFrame criado com sucesso")
print(df)

#salvar o resultado no diretorio D
df.to_csv("steam_sales.csv", index=False)
logging.info("Arquivo CSV gerado com sucesso")
