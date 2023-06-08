import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import csv

# Caminho do arquivo CSV
csv_file = "resultados.csv"

# Configuração do driver do Selenium (utilizando o Chrome)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome("./chromedriver", options=chrome_options)

# Acessa a página desejada
url = "https://csgo500.com/pt/wheel"

# Definindo o tempo de execução em segundos
tempo_execucao = 30

# Acessa a página
driver.get(url)
time.sleep(tempo_execucao)
# Loop para executar o web scraping a cada 30 segundos
while True:
    # Obtém o HTML da página atual
    html = driver.page_source

    # Parseia o HTML com o BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")

    # Extrai os dados desejados com base na estrutura HTML
    
    results = soup.find(attrs={"role": "listitem"})
    class_value = results.get("class")[-1]
    print(class_value)

    # Abrir o arquivo CSV em modo de escrita
    with open("resultados.csv", "a", newline="") as file:
        writer = csv.writer(file)
        # Escrever os valores no arquivo CSV
        writer.writerow([class_value])

    # Aguarda 30 segundos antes da próxima iteração
    time.sleep(tempo_execucao)

# Encerra o driver do Selenium
driver.quit()
