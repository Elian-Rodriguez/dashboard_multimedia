from controller.Data_connection import obtener_conexion 


def Crear_pintor(Nombre:str,Apellido:str,Biografia:str):
    Nombre=Nombre.upper()
    Apellido=Apellido.upper()
    conexion = obtener_conexion()
    Consulta="""INSERT INTO bosdos6qw6vefrichu88.Autor"""
    Consulta+="""(Nombre_autor, Apellido, Breve_biografia)"""
    Consulta+=f"""VALUES( '{Nombre}', '{Apellido}', ' {Biografia}');"""
    with conexion.cursor() as cursor:
        cursor.execute(Consulta)
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRECTAMENTE EL INSERT DE {Nombre} {Apellido}")


def obtener_pintor():
    conexion = obtener_conexion()
    pintores = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idAutor, Nombre_autor, Apellido FROM bosdos6qw6vefrichu88.Autor; ")
        pintores = cursor.fetchall()
    conexion.close()
    return pintores

def eliminar_pintor(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM bosdos6qw6vefrichu88.Autor WHERE idAutor=%s", (id,))
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRETAMENTE EL DELETE DE {id}")

def actualizar_visualizacion(id):
    conexion = obtener_conexion()
    Consulta=f"UPDATE bosdos6qw6vefrichu88.Autor SET  Activo=0 WHERE idAutor={id};"
    with conexion.cursor() as cursor:
        cursor.execute(Consulta)
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRECTAMENTE EL UPDATE DE {id} ")

def obtener_pintor_visual():
    conexion = obtener_conexion()
    pintores = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT idAutor, Nombre_autor, Apellido FROM bosdos6qw6vefrichu88.Autor WHERE Activo =1; ")
        pintores = cursor.fetchall()
    conexion.close()
    return pintores

def obtener_unico_pintor(id):
    conexion = obtener_conexion()
    pintores = []
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT * FROM bosdos6qw6vefrichu88.Autor WHERE idAutor ={id}; ")
        pintores = cursor.fetchall()
    conexion.close()
    print(str(pintores))
    return pintores

def actualizar_pintor(Nombre:str,Apellido:str,Biografia:str,id):
    conexion = obtener_conexion()
    Nombre=Nombre.upper()
    Apellido=Apellido.upper()
    Consulta=f"UPDATE bosdos6qw6vefrichu88.Autor SET Nombre_autor='{Nombre}', Apellido='{Apellido}', Breve_biografia='{Biografia}'  WHERE idAutor={id};"
    with conexion.cursor() as cursor:
        cursor.execute(Consulta)
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRECTAMENTE EL UPDATE DE {Nombre} {Apellido} ")

