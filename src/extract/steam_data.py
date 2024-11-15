import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

# Caminho para o geckodriver
geckodriver_path = r'D:\\biblioteca_projeto\\geckodriver.exe'

# Criando o serviço para o Firefox
service = Service(geckodriver_path)

# Inicializando o WebDriver com o serviço
driver = webdriver.Firefox(service=service)

# Acessando o site
driver.get('https://steamdb.info/sales/')