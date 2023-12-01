from bs4 import BeautifulSoup
import requests

pagina = requests.get("https://noticias.uol.com.br/")
site = BeautifulSoup(pagina.content, 'html.parser')

notici = site.find_all('div', attrs={'class':'thumb-caption'})

noti = [i.find('h3').text for i in notici]

noticia = noti[0:10:1]
noticia_1 = noticia[0]
noticia_2 = noticia[1]
noticia_3 = noticia[2]
noticia_4 = noticia[3]
noticia_5 = noticia[4]
noticia_6 = noticia[5]
noticia_7 = noticia[6]
noticia_8 = noticia[7]
noticia_9 = noticia[8]
noticia_10 = noticia[9]


print(f'''bem-vindo as ultimas noticias do mundo,\n
      noticia 1 : {noticia_1},\n 
      noticia 2 : {noticia_2},\n
      noticia 3 : {noticia_3},\n 
      noticia 4 : {noticia_4},\n
      noticia 5 : {noticia_5},\n 
      noticia 6 : {noticia_6},\n
      noticia 7 : {noticia_7},\n 
      noticia 8 : {noticia_8},\n
      noticia 9 : {noticia_9},\n 
      noticia 10 : {noticia_10}''')
