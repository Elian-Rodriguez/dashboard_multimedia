from controller.Data_connection import obtener_conexion 


def crearRespuesta(respuesta:str,correcta:int,id_pregunta:str):
    respuesta=respuesta.upper()
    
    conexion = obtener_conexion()
    Consulta=f"""INSERT INTO bosdos6qw6vefrichu88.Respuestas
                ( respuesta_var, Es_correcta, questions_idquestions)
                    VALUES('{respuesta}', {correcta}, {id_pregunta});
    """
    with conexion.cursor() as cursor:
        cursor.execute(Consulta)
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRECTAMENTE EL INSERT DE LA PREGUNTA '{respuesta}'")


def obtenerRespuestas():
    conexion = obtener_conexion()
    respuestas = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM bosdos6qw6vefrichu88.Respuestas ; ")
        respuestas = cursor.fetchall()
    conexion.close()
    return respuestas

def eliminarRespuesta(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM bosdos6qw6vefrichu88.Respuestas WHERE idRespuestas=%s", (id))
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRETAMENTE EL DELETE DE {id}")

def obtenerVisualRespuesta():
    conexion = obtener_conexion()
    respuestas=[]
    consulta="""SELECT idRespuestas ,q.pregunta_var ,r.respuesta_var ,r.Es_correcta  FROM bosdos6qw6vefrichu88.Respuestas r 
                inner join bosdos6qw6vefrichu88.questions q  on(r.questions_idquestions=q.idquestions )
                ORDER  by idRespuestas ,questions_idquestions ,Es_correcta desc;
    """
    with conexion.cursor()as cursor:
        cursor.execute(str(consulta))
        respuestas= cursor.fetchall()
    conexion.close()
    return respuestas

def ontenerUnicaRespuesta(id):
    conexion = obtener_conexion()
    pintores = []
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT * FROM bosdos6qw6vefrichu88.questions WHERE idRespuestas ={id}; ")
        pintores = cursor.fetchall()
    conexion.close()
    print(str(pintores))
    return pintores

def actualizarRespuesta(respuesta:str,correcta:int,id_pregunta:int,id_respuesta:int):
    conexion = obtener_conexion()
    Nombre=Nombre.upper()
    Consulta=f"""UPDATE bosdos6qw6vefrichu88.Respuestas
                SET respuesta_var='{respuesta}', Es_correcta={correcta}, questions_idquestions={id_pregunta}
                WHERE idRespuestas={id_respuesta};
                """
    with conexion.cursor() as cursor:
        cursor.execute(Consulta)
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRECTAMENTE EL UPDATE DE {Nombre} ")

def obtenerRespuestasPregunta(id_pregunta):
    conexion = obtener_conexion()
    respuestas=[]
    consulta=f"""SELECT * FROM bosdos6qw6vefrichu88.Respuestas WHERE questions_idquestions ={id_pregunta} ;
    """
    with conexion.cursor()as cursor:
        cursor.execute(str(consulta))
        respuestas= cursor.fetchall()
    conexion.close()
    return respuestas

def validarRespuesta(idRespuesta):
    conexion = obtener_conexion()
    consulta=f"SELECT Es_correcta FROM bosdos6qw6vefrichu88.Respuestas where idRespuestas  = {idRespuesta} ;"
    with conexion.cursor()as cursor:
        cursor.execute(str(consulta))
        respuestas= cursor.fetchone()
        conexion.close()
        #print(str(respuestas[0]))
    return int(respuestas[0])