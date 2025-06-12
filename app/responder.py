#Recebe a pergunta e a URL do site, busca o conteúdo do site, 
#Monta um prompt para a IA e consulta a API do OpenRouter para obter uma resposta baseada no conteúdo extraído.

# Importa as bibliotecas necessárias para fazer requisições HTTP e manipular JSON
import requests
import json

# Importa a função que faz o scraping do site e retorna o texto extraído
from app.crawler import obter_conteudo_site

# Chave de autenticação para acessar a API do OpenRouter (NUNCA compartilhe publicamente em produção)
OPENROUTER_API_KEY = ""

def responder_com_base_no_site(pergunta, url):
    """
    Função principal que:
    1. Busca o texto do site informado.
    2. Monta um prompt (instrução) para a IA, incluindo o texto do site e a pergunta do usuário.
    3. Envia esse prompt para a API do OpenRouter.
    4. Retorna a resposta gerada pela IA.
    """

    # Busca o texto do site usando o crawler
    texto = obter_conteudo_site(url)

    # Limita o texto para não ultrapassar o limite de tokens/caracteres da API
    texto_limitado = texto[:600]

    # Monta o prompt para a IA, orientando como ela deve responder
    prompt = (
        f"Se o usuario falar 'ola' ou 'oi', responda com 'Olá, como posso ajudar?'\n"
        f"Se o usuario falar 'tchau'' ou 'adeus', responda com 'Tchau, até mais!'\n"
        f"Seja educado e responda de forma clara e objetiva.\n"
        f"Verifique imagens da pagina e responda com base nas informações contidas nelas.\n"
        f"Você é um assistente virtual treinado para responder perguntas com base em informações extraídas de um site específico.\n"
        f"Você deve navegar pelo site e extrair informações relevantes para responder à pergunta do usuário.\n"
        f"Você deve considerar apenas as informações extraídas do site e não deve inventar respostas.\n"
        f"Informações do site:\n\"\"\"\n{texto_limitado}\n\"\"\"\n"
        f"Pergunta: {pergunta}\n"
    )

    # Define a URL da API do OpenRouter
    url_api = "https://openrouter.ai/api/v1/chat/completions"

    # Define os headers da requisição, incluindo a chave de autenticação
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    # Monta o corpo da requisição (payload) com o modelo e o prompt
    data = {
        "model": "deepseek/deepseek-r1:free",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    # Tenta enviar a requisição para a API e retorna a resposta da IA
    try:
        response = requests.post(
            url_api,
            headers=headers,
            data=json.dumps(data),
            timeout=30
        )
        response.raise_for_status()  # Lança erro se a resposta for ruim (ex: 401, 500)
        resposta = response.json()   # Converte a resposta JSON em dicionário Python
        # Extrai o texto da resposta gerada pela IA
        return resposta["choices"][0]["message"]["content"]
    except Exception as e:
        # Em caso de erro, retorna uma mensagem informando o erro
        return f"Erro ao consultar OpenRouter: {e}"