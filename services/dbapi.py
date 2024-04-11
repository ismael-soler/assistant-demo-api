import logging
import os
import time

import requests
from flask import request
from db_connection import getClient

# from utils.parser.parser import parse_predictions
# from utils.tensorflow import preprocess

# from exceptions.unauthorized import Unauthorized
# from exceptions.watson_error import WatsonError

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