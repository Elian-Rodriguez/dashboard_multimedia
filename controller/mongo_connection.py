import pymongo
import datetime
from dotenv import load_dotenv
import os

load_dotenv() 
coleccionDB = os.getenv('mongodbColection')

def obtenerConexionMongo():
    client = pymongo.MongoClient(os.getenv('client'))
    db = client.test
    return client

def obtenerDataBase():
    client = obtenerConexionMongo()
    db = client[coleccionDB]
    return db['RATINGS']

def insertNote(name: str, grado, idPregunta, idRespuesta, idPintura, puntaje):
    myclient = obtenerConexionMongo()
    mydb = myclient[coleccionDB]
    mycol = mydb["RATINGS"]
    name = name.upper()
    idPregunta = int(idPregunta)
    idRespuesta = int(idRespuesta)
    # Obtener la fecha actual
    fecha_actual = datetime.datetime.now()
    # Convertir la fecha actual a una cadena de texto en el formato ISO requerido por MongoDB
    fecha_actual_str = fecha_actual.isoformat()
    new_show = {
        "name": name,
        "grado": grado,
        "date": fecha_actual_str,
        "idPregunta": idPregunta,
        "idRespuesta": idRespuesta,
        "idPintura": idPintura,
        "Puntaje": puntaje
    }
    return mycol.insert_one(new_show).inserted_id

print(obtenerConexionMongo())
