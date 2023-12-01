from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
import time

paulista_lista = ['campeonato-paulista', 'campeonato-paulista-2022', 'campeonato-paulista-2021', 'campeonato-paulista-2020',
                  'campeonato-paulista-2019', 'campeonato-paulista-2018', 'campeonato-paulista-2017', 'campeonato-paulista-2016',
                  'campeonato-paulista-2015', 'campeonato-paulista-2014', 'campeonato-paulista-2013', 'campeonato-paulista-2012',
                  'campeonato-paulista-2011', 'campeonato-paulista-2010', 'campeonato-paulista-2009', 'campeonato-paulista-2008',
                  'campeonato-paulista-2007', 'campeonato-paulista-2006', 'campeonato-paulista-2005', 'campeonato-paulista-2004', 'campeonato-paulista-2003']

caminho_chromedriver = r"./chromedriver.exe"
servico = Service(caminho_chromedriver)
driver = webdriver.Chrome(service=servico)
espera = WebDriverWait(driver, 100)

# Criar um DataFrame vazio
dados_finais = pd.DataFrame()

for paulista in paulista_lista:
    driver.get(f"https://www.flashscore.com.br/futebol/brasil/{paulista}/resultados/")
    time.sleep(20)

    casa = driver.find_elements(By.CLASS_NAME, 'event__participant--home')
    visitante = driver.find_elements(By.CLASS_NAME, 'event__participant--away')
    fthg = driver.find_elements(By.CLASS_NAME, 'event__score--home')
    ftag = driver.find_elements(By.CLASS_NAME, 'event__score--away')
    data = driver.find_elements(By.CLASS_NAME, 'event__time')

    Mandante = []
    Visitante = []
    FTHG = []
    FTAG = []
    Data = []

    for link in casa:
        texto_link = link.text.strip()
        if texto_link:
            Mandante.append(texto_link)

    for link in visitante:
        texto_link = link.text.strip()
        if texto_link:
            Visitante.append(texto_link)

    for link in fthg:
        texto_link = link.text.strip()
        if texto_link:
            FTHG.append(texto_link)

    for link in ftag:
        texto_link = link.text.strip()
        if texto_link:
            FTAG.append(texto_link)

    for link in data:
        texto_link = link.text.strip()
        if texto_link:
            Data.append(texto_link)

    # Criar um DataFrame para a iteração atual
    dados_iteracao = pd.DataFrame({
        'Mandante': Mandante,
        'Visitante': Visitante,
        'FTHG': FTHG,
        'FTAG': FTAG,
        'Data': Data
    })

    # Concatenar os dados da iteração ao DataFrame final
    dados_finais = pd.concat([dados_finais, dados_iteracao], ignore_index=True)

# Salvar o DataFrame final em um arquivo CSV
dados_finais.to_excel('paulista.xlsx', index=False)

# Fechar o WebDriver após o loop
driver.quit()
