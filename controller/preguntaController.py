from controller.Data_connection import obtener_conexion 


def crearPregunta(pregunta:str,id_pintura:int):
    pregunta=pregunta.upper()
    
    conexion = obtener_conexion()
    Consulta="""INSERT INTO  bosdos6qw6vefrichu88.questions"""
    Consulta+="""(pregunta_var,Pintura_idPintura)"""
    Consulta+=f"""VALUES( '{pregunta}',{id_pintura});"""
    with conexion.cursor() as cursor:
        cursor.execute(Consulta)
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRECTAMENTE EL INSERT DE LA PREGUNTA '{pregunta}'")


def obtenerPregunta():
    conexion = obtener_conexion()
    preguntas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM bosdos6qw6vefrichu88.questions  ; ")
        preguntas = cursor.fetchall()
    conexion.close()
    return preguntas

def eliminarPregunta(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM bosdos6qw6vefrichu88.questions WHERE idquestions=%s", (id))
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRETAMENTE EL DELETE DE {id}")


def ontenerUnicaPregunta(id):
    conexion = obtener_conexion()
    pintores = []
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT * FROM bosdos6qw6vefrichu88.questions WHERE idquestions ={id}; ")
        pintores = cursor.fetchall()
    conexion.close()
    print(str(pintores))
    return pintores

def actualizarContinente(Nombre:str,id):
    conexion = obtener_conexion()
    Nombre=Nombre.upper()
    Consulta=f"UPDATE bosdos6qw6vefrichu88.questions SET pregunta_var='{Nombre}'  WHERE idquestions={id};"
    with conexion.cursor() as cursor:
        cursor.execute(Consulta)
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRECTAMENTE EL UPDATE DE {Nombre} ")

def preguntasCreadas():
    conexion = obtener_conexion()
    Preguntas = []
    Consulta ="""SELECT q.idquestions , p.Nombre_pintura ,q.pregunta_var  ,count(r.questions_idquestions) as Respuestas_registradas
FROM bosdos6qw6vefrichu88.questions q 
inner join bosdos6qw6vefrichu88.Pintura p on(q.Pintura_idPintura=p.idPintura)
LEFT OUTER  JOIN  bosdos6qw6vefrichu88.Respuestas r on(q.idquestions=r.questions_idquestions)
GROUP BY q.idquestions;
    """
    with conexion.cursor() as cursor:
        cursor.execute(Consulta)
        Preguntas=cursor.fetchall()
    conexion.close()
    return Preguntas