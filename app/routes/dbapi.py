from flask import Blueprint, jsonify

from services import dbapi

dbapi_routes = Blueprint('dbapi_routes', __name__)

@dbapi_routes.route('/', methods=['GET'])
def okay():
    return dbapi.okay()

@dbapi_routes.route('/getAll', methods=['GET'])
# @cross_origin()
def getAllUsers():
    return dbapi.getAllUsers()

@dbapi_routes.route('/id/<userID>', methods=['GET'])
# @cross_origin()
def getUserByID(userID):
    return dbapi.getUserByID(userID)

@dbapi_routes.route('/getAllByCitizenID/<citID>', methods=['GET'])
# @cross_origin()
def getUserByCitID(citID):
    return dbapi.getUserByCitID(citID)

@dbapi_routes.route('/getBalanceByCitizenId/<citID>', methods=['GET'])
# @cross_origin()
def getBalanceByCitizenID(citID):
    return dbapi.getBalanceByCitizenID(citID)

@dbapi_routes.route('/getDebtByCitizenId/<citID>', methods=['GET'])
# @cross_origin()
def getDebtByCitizenID(citID):
    return dbapi.getDebtByCitizenID(citID)

@dbapi_routes.route('/getNameByCitizenId/<citID>', methods=['GET'])
# @cross_origin()
def getNameByCitizenID(citID):
    return dbapi.getNameByCitizenID(citID)

@dbapi_routes.route('/isIDValid/<citID>', methods=['GET'])
# @cross_origin()
def isIDValid(citID):
    return dbapi.isIDValid(citID)