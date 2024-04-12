from flask import request, jsonify
from db_connection import getClient

def okay():
    return "okay"

# Get all users
def getAllUsers():
    cursor = getClient()
    cursor.execute("SELECT * FROM myTable")
    result = cursor.fetchall()
    return result

# Get user by DB ID
def getUserByID(userID):
    cursor = getClient()
    cursor.execute(f"SELECT * FROM myTable WHERE id = {userID};")
    result = cursor.fetchall()
    return result

# Get user by citizenship ID
def getUserByCitID(citID):
    cursor = getClient()
    cursor.execute(f"SELECT * FROM myTable WHERE citizenship_id = {citID};")
    result = cursor.fetchall()
    print(type(result))
    return result

def getBalanceByCitizenID(citID):
    cursor = getClient()
    cursor.execute(f"SELECT balance FROM myTable WHERE citizenship_id = {citID};")
    result = cursor.fetchall()[0]
    return result[0]

def getDebtByCitizenID(citID):
    cursor = getClient()
    cursor.execute(f"SELECT debt FROM myTable WHERE citizenship_id = {citID};")
    result = cursor.fetchall()[0]
    return result[0]

def getNameByCitizenID(citID):
    cursor = getClient()
    cursor.execute(f"SELECT name, surname FROM myTable WHERE citizenship_id = {citID};")
    result = cursor.fetchall()[0]
    nameStr = f"{result[0]} {result[1]}"
    return nameStr

def isIDValid(citID):
    cursor = getClient()
    cursor.execute(f"SELECT 1 FROM myTable WHERE citizenship_id = {citID};")
    result = cursor.fetchall()
    return jsonify({"isValid": bool(result)})
