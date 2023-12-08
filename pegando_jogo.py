from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import time

caminho_chromedriver = r"./chromedriver.exe"
servico = Service(caminho_chromedriver)
driver = webdriver.Chrome(service=servico)
espera = WebDriverWait(driver, 100)

# Criar um DataFrame vazio
dia = int(input("digite um numero correspondente:"))


driver.get(f"https://footballpredictions.net/pt/prognosticos-gratuitos-dicas-apostas-futebol-{dia}-dias")
time.sleep(20)

casa = driver.find_elements(By.CLASS_NAME, 'team-label')

jogos = []

for link in casa:
        texto_link = link.text.strip()
        if texto_link:
            jogos.append(texto_link)
            
casa = jogos[0:20:2]
vizitante = jogos[1:20:2]

jogos_dia = pd.DataFrame({
        'casa': casa,
        'Visitante': vizitante})

print(jogos_dia)

