import mysql.connector
import os
from dotenv import load_dotenv, dotenv_values 


load_dotenv()
def connectToClient():


    mydb = mysql.connector.connect(
        host=os.environ.get('DB_HOST'),
        user=os.environ.get('DB_USER'),
        port=os.environ.get('DB_PORT'),
        password=os.environ.get('DB_PASSWORD'),
        ssl_ca=os.environ.get('DB_SSL_CA'),
        ssl_verify_cert=True,
        ssl_verify_identity=True,
        database=os.environ.get('DB_DATABASE')
        )
    return mydb

def getClient():
    return mydb.cursor()

mydb = connectToClient()