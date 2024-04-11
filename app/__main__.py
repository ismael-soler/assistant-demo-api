from flask import Flask
from app.db_connection import connectToClient
import os
from app.db_connection import connectToClient

environment = os.environ.get('FLASK_ENV')

import routes

def createApp():
    app = Flask(__name__)
    # Init blueprints

    routes.initApp(app)
    connectToClient()
    return app

def init(app):
    port = int(os.getenv("PORT", 8080))

    if environment == 'production':
        from waitress import serve
        serve(app, host="0.0.0.0", port=8080)
    else:
        app.run(host='0.0.0.0', port=port)
    # app.run()

if (__name__) == '__main__':
    init(createApp())