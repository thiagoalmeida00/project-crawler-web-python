#UNIFACISA - CENTRO UNIVERSITÁRIO
#SISTEMAS DE INFORMAÇÃO
#DISCIPLINA: PROGRAMAÇÃO 1
#PROFESSOR: JEMERSON DAMÁSIO
#EQUIPE: THIAGO LEANDRO ALMEIDA & THIAGO AZEVEDO SOARES
#MATRÍCULA: 2023080006 & 2023081065 / TURNO: MANHÃ

#>>>>>>>>>>>>>>>>>> PROJETO DE PROGRAMAÇÃO 1 - CRAWLER #<<<<<<<<<<<<<<<<<<<<<<
#CRAWLER

#Importando as bibliotecas necessárias para processamento do Crawler e
#armazenamento em arquivos (escrita, leitura e carregamento)
import json
import requests
import re
from bs4 import BeautifulSoup

#url's utilizados no projeto:
#>>> 'https://jovempan.com.br/'
#>>> 'http://www.radiorock.com.br/'
#>>> 'https://www.rollingstone.com/'
#>>> 'https://www.uol.com.br/'

site_semente = 'https://jovempan.com.br/'

try:
    url = requests.get(site_semente)
    fonte_links = url.content
    soup_links = BeautifulSoup(fonte_links, 'html.parser')

    #Para obter a lista de links presentes no site_semente:
    lista_links = [site_semente]
    links_site = soup_links.find_all('a', attrs={'href': re.compile('^http')})

except:
    print ('Erro ao acessar o conteúdo desta página.')

prof_atual = 0
prof_limite = 1

while prof_atual < prof_limite:
    try:
        for link in links_site:
            lista_links.append(link.get('href'))

    except:
        print ('Erro ao acessar o conteúdo desta página: (%s)' % link)
    
    prof_atual += 1

lista_liquida = list(set(lista_links))

with open('sites_jovempan.json', 'w') as outfile: 
    json.dump(lista_liquida, outfile)
outfile.close()

#Para obter o texto presente em cada link da lista_liquida:
conteudo = {}
cont = 0
pos = 0

while cont < len(lista_liquida):
    try:
        url = requests.get(lista_liquida[pos])
        fonte_texto = url.text
        soup_texto = BeautifulSoup(fonte_texto, 'html.parser')
        texto_site = soup_texto.get_text().lower()
        conteudo[lista_liquida[pos]] = texto_site.split()

        pos += 1
    except:
        print ('Erro ao acessar o conteúdo desta página: (%s)' % (lista_liquida[pos]))

    cont += 1    

    with open('data_jovempan.json', 'w') as outfile: 
        json.dump(conteudo, outfile)
    outfile.close()
