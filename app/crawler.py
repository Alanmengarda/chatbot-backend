import requests
from bs4 import BeautifulSoup

def obter_conteudo_site(url):
    """
    Faz uma requisição HTTP para o site e retorna o texto visível da página.
    """
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.text, 'html.parser')
    textos = soup.stripped_strings
    return ' '.join(textos)