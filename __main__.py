from flask import Flask
import os

environment = os.environ.get('FLASK_ENV')

import routes

def create_app():
    app = Flask(__name__)
    # Init blueprints
    routes.init_app(app)
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
    init(create_app())