from flask import Blueprint, jsonify

from services import dbapi

dbapi_routes = Blueprint('dbapi_routes', __name__)

@dbapi_routes.route('/test', methods=['GET'])
# @cross_origin()
def test():
    return dbapi.test()
