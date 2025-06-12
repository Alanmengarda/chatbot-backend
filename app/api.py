#Define a rota da API que recebe perguntas do frontend
#Chama a função de resposta e retorna a resposta em JSON.

from flask import Blueprint, request, jsonify
from app.responder import responder_com_base_no_site

chatbot_api = Blueprint('chatbot_api', __name__) #Blueprint Permite organizar as rotas da API separadamente.

@chatbot_api.route('/chat', methods=['POST']) #Rota que recebe a pergunta do usuário.
def chat():
    data = request.get_json()
    pergunta = data.get('pergunta', '')
    url = "https://www.jovemprogramador.com.br"  # Coloque aqui o site desejado
    resposta = responder_com_base_no_site(pergunta, url) #Chama a função que busca a resposta baseada no conteúdo do site.
    return jsonify({'resposta': resposta})