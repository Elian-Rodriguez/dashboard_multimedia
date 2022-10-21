import pymongo

# Create the client
def obtenerConexionMongo():
    client = pymongo.MongoClient("mongodb+srv://alien_83:Arelis11@cluster0.4ur0oyq.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    return client
def obtenerDataBase():
    client =  obtenerConexionMongo()
    db = client['SeriesDB']
    # Fetch our series collection
    return  db['series']

def insertDocument(collection, data):
    """ Function to insert a document into a collection and
    return the document's id.
    """
    return collection.insert_one(data).inserted_id

def insertNote(name:str,idPregunta,idRespuesta):
    name = name.upper()
    idPregunta=int(idPregunta)
    idRespuesta=int(idRespuesta)
    new_show = {
    "name": name,
    "year": 1994
    }
    return (insertDocument(obtenerDataBase(), new_show))
    