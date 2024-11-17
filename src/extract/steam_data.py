import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import logging
import time

# configuração do logging
logging.basicConfig(level=logging.INFO)

# caminho para o geckodriver
geckodriver_path = r'D:\\biblioteca_projeto\\geckodriver.exe'

# inicializando o WebDriver
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service)

# acessando o site onde devemos fazer o webscrapping
url = 'https://steamdb.info/sales/'
driver.get(url)

# lista que criei para armazenar os dados de todas as páginas
games = []

# loop para navegar entre as páginas (1 a 20)
for page in range(1, 21):
    # aguarda a tabela carregar
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "DataTables_Table_0"))
    )

    # extrai o conteúdo da página atual
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    
    # extraindo os dados da tabela
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
    
    # tantando clicar no botão da próxima página, exceto na ultima
    if page < 20:
        next_button = driver.find_element(By.CSS_SELECTOR, "button.dt-paging-button.next")
        next_button.click()
        time.sleep(2)  # da pequenos intervalo para a página carregar

# fechando o driver
driver.quit()

# friando o DataFrame
df = pd.DataFrame(games)
logging.info("DataFrame criado com sucesso")
print(df)

#salvar o resultado no diretorio D
df.to_csv("steam_sales.csv", index=False)
logging.info("Arquivo CSV gerado com sucesso")
