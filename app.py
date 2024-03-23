#!/usr/bin/env python3
from config import app
from models.models import *
from routes.routes import *
from integration.plaid_integration import plaid_bp 
from routes.two_fa_routes import two_fa_blueprint
from ai_api import open_ai


app.register_blueprint(plaid_bp, url_prefix='/plaid')
app.register_blueprint(open_ai, url_prefix='/openai')
app.register_blueprint(two_fa_blueprint, url_prefix='/2fa')


if __name__ == '__main__':
    app.run(port=5000, host="0.0.0.0", debug=True)