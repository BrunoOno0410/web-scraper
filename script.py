import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# Caminho do arquivo CSV
csv_file = "resultados.csv"  # Arquivo criado para salvar resultados

# Configuração do driver do Selenium (utilizando o Chrome)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(
    "./chromedriver", options=chrome_options  # Configurar caminho do driver
)
# ./chromedriver padrão (executável na mesma pasta do script)

# Acessa a página desejada
url = "link-desejado-aqui"  # Colocar site desejado

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
    class_value = results.get("class")[-1]
    # Pegar última palavra da classe (resultado) = "black, red, blue, yellow"
    results = soup.find(attrs={"role": "listitem"})

    array = []
    array.append(class_value)
    print(array)

    # Abrir o arquivo CSV em modo de escrita
    with open(csv_file, "w", newline="") as file:
        writer = csv_file.writer(file)
        # Escrever os valores no arquivo CSV
        writer.writerow(array)

    # Aguarda 30 segundos antes da próxima iteração
    time.sleep(tempo_execucao)

# Encerra o driver do Selenium
driver.quit()
