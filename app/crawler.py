#Faz o scraping (extração) do texto do site (e pode ser adaptado para seguir links internos e/ou descrever imagens).

import os
import requests
from bs4 import BeautifulSoup

def salvar_conteudo(conteudo):
    os.makedirs('data', exist_ok=True)
    with open('data/content.txt', 'w', encoding='utf-8') as f:
        f.write(conteudo)

def obter_conteudo_site(url): #Faz uma requisição HTTP para o site. 
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.text, 'html.parser') #Usa BeautifulSoup para extrair todo o texto visível da página.
    textos = soup.stripped_strings
    return ' '.join(textos) #Retorna o texto concatenado.