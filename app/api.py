from flask import Blueprint, request, jsonify
from app.responder import responder_com_base_site_arquivo

chatbot_api = Blueprint('chatbot_api', __name__)

@chatbot_api.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    pergunta = data.get('pergunta', '')
    url = "https://www.jovemprogramador.com.br"  # Ou outro site desejado
    caminho_arquivo = "content.txt"
    resposta = responder_com_base_site_arquivo(pergunta, url, caminho_arquivo)
    return jsonify({'resposta': resposta})