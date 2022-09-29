from controller.Data_connection import obtener_conexion 


def crearPieza(Id_ubicacion_parte:int,parte:str,Pintura_idPintura:int):    
    conexion = obtener_conexion()
    Consulta="""INSERT INTO bosdos6qw6vefrichu88.puzzle_part"""
    Consulta+="""(Id_ubicacion_parte, parte, Pintura_idPintura)"""
    Consulta+=f"""VALUES({Id_ubicacion_parte}, '{parte}', {Pintura_idPintura});;"""
    with conexion.cursor() as cursor:
        cursor.execute(Consulta)
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRECTAMENTE EL INSERT DE {parte}")


def obtenerTodasPartes():
    conexion = obtener_conexion()
    partes = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM bosdos6qw6vefrichu88.puzzle_part  ; ")
        partes = cursor.fetchall()
    conexion.close()
    return partes

def obtenerUnicaParte(id):
    conexion = obtener_conexion()
    pintores = []
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT * FROM bosdos6qw6vefrichu88.puzzle_part WHERE idpuzzle_part ={id}; ")
        pintores = cursor.fetchone()
    conexion.close()
    print(str(pintores))
    return pintores

def obtenerPartesPintura(id_pintura):
    conexion = obtener_conexion()
    partesRompecabezas=[]
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT * FROM bosdos6qw6vefrichu88.puzzle_part WHERE Pintura_idPintura = {id_pintura} ;")
        partesRompecabezas=cursor.fetchall()
    conexion.close()
    return partesRompecabezas
