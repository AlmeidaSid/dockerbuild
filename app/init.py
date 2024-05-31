from flask import Flask

def create_app():
    app = Flask(__name__)

    # Importa e registra as rotas do app
    from .main import resultados_nba
    app.register_blueprint(resultados_nba)

    return app