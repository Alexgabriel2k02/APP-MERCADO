from flask import Flask

def create_app():
    app = Flask(__name__)
    # Configurações e rotas podem ser adicionadas aqui
    return app