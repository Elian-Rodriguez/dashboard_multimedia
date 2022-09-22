from controller.Data_connection import obtener_conexion 


def crearEstilo(Nombre:str,Descripcion_estilo:str):
    Nombre=Nombre.upper()
    
    conexion = obtener_conexion()
    #idEstilos_pintura	Nombre_estilo	Descripcion_estilo
    Consulta="""INSERT INTO  bosdos6qw6vefrichu88.Estilos_pintura"""
    Consulta+="""(Nombre_estilo,Descripcion_estilo)"""
    Consulta+=f"""VALUES( '{Nombre}','{Descripcion_estilo}');"""
    with conexion.cursor() as cursor:
        cursor.execute(Consulta)
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRECTAMENTE EL INSERT DE {Nombre}")


def obtenerEstilo():
    conexion = obtener_conexion()
    estilo = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM bosdos6qw6vefrichu88.Estilos_pintura  ; ")
        estilo = cursor.fetchall()
    conexion.close()
    return estilo

def eliminarEstilo(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM bosdos6qw6vefrichu88.Estilos_pintura WHERE idEstilos_pintura=%s", (id))
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRETAMENTE EL DELETE DE {id}")


def obtenerVisualEstilo():
    conexion = obtener_conexion()
    estilo = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM bosdos6qw6vefrichu88.Estilos_pintura  ; ")
        estilo = cursor.fetchall()
    conexion.close()
    return estilo

def ontenerUnicoEstilo(id):
    conexion = obtener_conexion()
    estilo = []
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT * FROM bosdos6qw6vefrichu88.Estilos_pintura WHERE idEstilos_pintura ={id}; ")
        estilo = cursor.fetchall()
    conexion.close()
    print(str(estilo))
    return estilo

def actualizarEstilo(Nombre:str,Descripcion_estilo:str,id):
    #idEstilos_pintura	Nombre_estilo	Descripcion_estilo
    conexion = obtener_conexion()
    Nombre=Nombre.upper()
    Consulta=f"UPDATE bosdos6qw6vefrichu88.Estilos_pintura SET Nombre_estilo='{Nombre}' ,Descripcion_estilo='{Descripcion_estilo}' WHERE idEstilos_pintura={id};"
    with conexion.cursor() as cursor:
        cursor.execute(Consulta)
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRECTAMENTE EL UPDATE DE {Nombre} ")

