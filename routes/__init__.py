from .dbapi import dbapi_routes

def initApp(app):
    app.register_blueprint(dbapi_routes)