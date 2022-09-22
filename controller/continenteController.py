from controller.Data_connection import obtener_conexion 


def crearContinentw(Nombre:str):
    Nombre=Nombre.upper()
    
    conexion = obtener_conexion()
    Consulta="""INSERT INTO  bosdos6qw6vefrichu88.Continente"""
    Consulta+="""(Nombre_continente)"""
    Consulta+=f"""VALUES( '{Nombre}');"""
    with conexion.cursor() as cursor:
        cursor.execute(Consulta)
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRECTAMENTE EL INSERT DE {Nombre}")


def obtenerContinente():
    conexion = obtener_conexion()
    pintores = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM bosdos6qw6vefrichu88.Continente  ; ")
        pintores = cursor.fetchall()
    conexion.close()
    return pintores

def eliminarContinente(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM bosdos6qw6vefrichu88.Continente WHERE idContinente=%s", (id))
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRETAMENTE EL DELETE DE {id}")


def obtenerVisualContinente():
    conexion = obtener_conexion()
    pintores = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM bosdos6qw6vefrichu88.Continente  ; ")
        pintores = cursor.fetchall()
    conexion.close()
    return pintores

def ontenerUnicoContinente(id):
    conexion = obtener_conexion()
    pintores = []
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT * FROM bosdos6qw6vefrichu88.Continente WHERE idContinente ={id}; ")
        pintores = cursor.fetchall()
    conexion.close()
    print(str(pintores))
    return pintores

def actualizarContinente(Nombre:str,id):
    conexion = obtener_conexion()
    Nombre=Nombre.upper()
    Consulta=f"UPDATE bosdos6qw6vefrichu88.Continente SET Nombre_continente='{Nombre}'  WHERE idContinente={id};"
    with conexion.cursor() as cursor:
        cursor.execute(Consulta)
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRECTAMENTE EL UPDATE DE {Nombre} ")

