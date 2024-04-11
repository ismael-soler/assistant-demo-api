from .dbapi import dbapi_routes

def init_app(app):
    app.register_blueprint(dbapi_routes)