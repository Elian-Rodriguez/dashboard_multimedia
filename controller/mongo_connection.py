import pymongo
import datetime

from dotenv import load_dotenv
import os
load_dotenv() 

# Create the client
def obtenerConexionMongo():
    client = pymongo.MongoClient(os.getenv('client'))
    db = client.test
    print(db)
    return client
def obtenerDataBase():
    client =  obtenerConexionMongo()
    
    db = client['ART_QUALIFICATION']
    # Fetch our series collection
    return  db['RATINGS']

def insertDocument(collection, data):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id

def insertNote(name:str,grado,idPregunta,idRespuesta,idPintura,puntaje):
    myclient=obtenerConexionMongo()
    mydb = myclient["ART_QUALIFICATION"]
    mycol = mydb["QUALIFICATION"]
    name = name.upper()
    idPregunta=int(idPregunta)
    idRespuesta=int(idRespuesta)
    d = datetime.datetime.strptime("2017-10-13T10:53:53.000Z", "%Y-%m-%dT%H:%M:%S.000Z")

    new_show = {
    "name": name,
    "grado":grado,
    "date" : d,
    "idPregunta": idPregunta,
    "idRespuesta":idRespuesta,
    "idPintura":idPintura,
    "Puntaje":puntaje
    }
    
    return mycol.insert_one(new_show).inserted_id
