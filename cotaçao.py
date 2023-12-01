from bs4 import BeautifulSoup
import requests
import pandas as pd

pagina = requests.get("https://br.investing.com/currencies/streaming-forex-rates-majors")
site = BeautifulSoup(pagina.content, 'html.parser')

notici = site.find_all('span', attrs={'class':'whitespace-nowrap'})

#contaçao = [i.find('whitespace-nowrap') for i in notici]
moedas1 = []

for span in notici:
    texto_link = span.text.strip()
    if texto_link:
        moedas1.append(texto_link)

compra = site.find_all('td', attrs={'class':'dynamic-table_col-other__Eu_RC'})

#contaçao = [i.find('whitespace-nowrap') for i in notici]
comprar = []

for td in compra:
    texto_link = td.text.strip()
    if texto_link:
        comprar.append(texto_link)
        

compra = comprar[0:301:7]
vender = comprar[1:301:7]
Máxima = comprar[2:301:7]
minima = comprar[3:301:7]
variaçao = comprar[4:301:7]
var_porce = comprar[5:301:7]
hora = comprar[6:301:7]
moedas = moedas1[0:43:1]

'''print(len(compra))
print(len(vender))
print(len(Máxima))
print(len(minima))
print(len(variaçao))
print(len(var_porce))
print(len(hora))
print(len(moedas))'''


contaçoes_moedas = pd.DataFrame({
        'moedas': moedas,
        'compra': compra,
        'vender': vender,
        'maxima': Máxima,
        'minima': minima,
        'variaçao':variaçao,
        'var_porce':var_porce,
        'hora':hora
    })

print(contaçoes_moedas)