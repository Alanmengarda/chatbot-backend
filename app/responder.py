import google.generativeai as genai
from app.crawler import obter_conteudo_site

# Substitua pela sua chave da API Gemini
GEMINI_API_KEY = "GOOGLE_API_KEY"

genai.configure(api_key=GEMINI_API_KEY)
model_name = "gemini-1.5-flash-latest"
model = genai.GenerativeModel(model_name)

def responder_com_base_site_arquivo(pergunta, url, caminho_arquivo="content.txt"):
    """
    Busca o texto do site e do arquivo, monta um prompt e usa a Gemini 1.5 Flash para responder.
    """
    try:
        # Busca conteúdo do site
        texto_site = obter_conteudo_site(url)
        if not texto_site:
            texto_site = "Não foi possível extrair informações do site."
        texto_site_limitado = texto_site[:1000]

        # Busca conteúdo do arquivo
        try:
            with open(caminho_arquivo, "r", encoding="utf-8") as f:
                texto_arquivo = f.read()
        except Exception:
            texto_arquivo = ""
        if not texto_arquivo:
            texto_arquivo = "O arquivo está vazio ou não foi possível ler o conteúdo."
        texto_arquivo_limitado = texto_arquivo[:1000]

        # Monta o prompt unindo as duas fontes
        prompt = (
            f"Você é um assistente virtual brasileiro. Use apenas as informações abaixo para responder à pergunta do usuário de forma clara, objetiva e em português.\n"
            f"Seja breve e direto, evitando repetições e informações irrelevantes.\n"
            f"Responda apenas com base nas informações fornecidas, sem adicionar opiniões ou informações externas.\n"
            f"Se a pergunta não puder ser respondida com as informações fornecidas, informe que não há dados suficientes.\n"
            f"Seja educado e profissional em suas respostas.\n"
            f"Limite suas respostas a 256 tokens.\n"
            f"No final de cada resposta, pergunte se o usuário precisa de mais alguma coisa.\n"
            f"Conteúdo do site ({url}):\n\"\"\"\n{texto_site_limitado}\n\"\"\"\n"
            f"Conteúdo do arquivo ({caminho_arquivo}):\n\"\"\"\n{texto_arquivo_limitado}\n\"\"\"\n"
            f"Pergunta: {pergunta}\n"
            f"Se o usuario falar algo como,'oi', 'olá', 'oi, tudo bem?', 'olá, tudo bem?' ou 'oi, tudo bem com você?', responda com uma saudação amigável e com a mensagem 'Como posso ajudar?'.\n"
            f"Responda apenas com base nas informações fornecidas."
        )

        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Ocorreu um erro ao processar sua solicitação: {e}"