#É o ponto de entrada da aplicação Flask. 
#Inicializa o servidor web, carrega o blueprint da API
#e define a rota principal para a interface web.

from flask import Flask, render_template
from app.api import chatbot_api

app = Flask(__name__)  #Cria a aplicação Flask.
app.register_blueprint(chatbot_api) #Registra as rotas da API.

@app.route("/") # Rota principal que renderiza o template index.html. / retorna a página HTML do chatbot.
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
"""

O usuário acessa o site e envia uma pergunta.
Frontend faz uma requisição POST para /chat com a pergunta.
API (api.py) recebe a pergunta, define o site a ser pesquisado e chama responder_com_base_no_site.
responder.py busca o conteúdo do site, monta o prompt e consulta a IA do OpenRouter.
A resposta da IA é enviada de volta para o frontend e exibida ao usuário.



"""