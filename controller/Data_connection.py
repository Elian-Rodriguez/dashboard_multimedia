import pymysql
from dotenv import load_dotenv
import os
load_dotenv() 

MYSQL_ADDON_HOST=os.getenv('MYSQL_ADDON_HOST')
MYSQL_ADDON_DB=os.getenv('MYSQL_ADDON_DB')
MYSQL_ADDON_USER=os.getenv('MYSQL_ADDON_USER')
MYSQL_ADDON_PORT=os.getenv('MYSQL_ADDON_PORT')
MYSQL_ADDON_PASSWORD=os.getenv('MYSQL_ADDON_PASSWORD')
MYSQL_ADDON_URI=os.getenv('MYSQL_ADDON_URI')
HOST=os.getenv('HOST')
DATA_BASE=os.getenv('DATA_BASE')


def obtener_conexion():
    return pymysql.connect(host=MYSQL_ADDON_HOST,
                                user=MYSQL_ADDON_USER,
                                password=MYSQL_ADDON_PASSWORD,
                                db=DATA_BASE)

#print(str(obtener_conexion()))