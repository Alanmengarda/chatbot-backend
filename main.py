#É o ponto de entrada da aplicação Flask. 
#Inicializa o servidor web, carrega o blueprint da API
#e define a rota principal para a interface web.

from flask import Flask, render_template
from app.api import chatbot_api

app = Flask(__name__)
app.register_blueprint(chatbot_api)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
