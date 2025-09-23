# backend/app.py
from flask import Flask
from flask_cors import CORS
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load all constants from Config

    CORS(app, resources={r"/ticker": {"origins": "http://localhost:port"}})

    # Register routes
    from routes.home import home_bp
    from routes.commodity import commodity_bp
    from routes.ticker import ticker_bp

    app.register_blueprint(home_bp)
    app.register_blueprint(commodity_bp)
    app.register_blueprint(ticker_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    from models.commodity import Commodity
    # Initialize all commodities
    commodity_list = [Commodity(path) for path in app.config['COMMODITY_DICT'].values()]
    app.run(debug=True)
