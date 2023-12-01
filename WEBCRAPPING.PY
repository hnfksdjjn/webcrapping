from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

import pyautogui
import time
import pandas as pd

#site = input("digite seu site com https:// \n")
pesquisa = input("digite o nome da cidade - estado: \n")

chromedriver_path = r"./chromedriver.exe"
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 100)

driver.get(f"https://www.tempo.com/{pesquisa}.htm")
time.sleep(3)

elements = driver.find_elements(By.XPATH, '//*[@id="btn-gdpr-accept"]')
if elements:
    elements[0].send_keys(Keys.ENTER)
else:
    print("No elements found with the specified XPath.")
time.sleep(2)

cidad = driver.find_elements(By.CLASS_NAME, 'text-princ')
tempo_ma = driver.find_elements(By.CLASS_NAME, 'max')
tempo_mi = driver.find_elements(By.CLASS_NAME, 'min')
descriç = driver.find_elements(By.CLASS_NAME, 'descripcion')
vent = driver.find_elements(By.CLASS_NAME, 'changeUnitW')
sens = driver.find_elements(By.CLASS_NAME, 'sensacion')


time.sleep(5)

cidader = []
tempo_1 = []
tempo_2 = []
descriçao = []
vento = []
sensaçao = []


for link in cidad:
    texto_link = link.text.strip()
    if texto_link:
        cidader.append(texto_link)

for link in tempo_ma:
    texto_link = link.text.strip()
    if texto_link:
        tempo_2.append(texto_link)

for link in tempo_mi:
    texto_link = link.text.strip()
    if texto_link:
        tempo_1.append(texto_link)
        
for link in descriç:
    texto_link = link.text.strip()
    if texto_link:
        descriçao.append(texto_link)

for link in sens:
    texto_link = link.text.strip()
    if texto_link:
        sensaçao.append(texto_link)

for link in vent:
    texto_link = link.text.strip()
    if texto_link:
        vento.append(texto_link)


cidade = cidader[0]
tempo_minimo = tempo_1[0]
tempo_maximo = tempo_2[0]
descricao = descriçao[0]
sensa = sensaçao[0]
vento_1 = vento[0]
vento_2 = vento[1]


print(f"o tempo na cidade de {pesquisa} o minimo esta {tempo_minimo} e o maximo {tempo_maximo} com a sensaçao de {sensa}, com o tempo {descricao}, com velocidade do vento de {vento_1} a {vento_2}")




#https://www.climatempo.com.br/class="general-search-input"