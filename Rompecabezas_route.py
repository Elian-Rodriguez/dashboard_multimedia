from multiprocessing import context
import controller.partPuzzleController as partPuzzleCm
import controller.pinturaController as pinturaC
import controller.pintorController as pintorC
import controller.estiloController as estiloC
import controller.preguntaController as preguntaC
import controller.respuestaController as respuestasC
from flask import Blueprint,render_template,request,session,url_for,redirect
import random
import numpy as np

Rompecabezas_Blueprint = Blueprint('Rompecabezas',__name__,template_folder='templates', static_folder='static')

@Rompecabezas_Blueprint.route('/Rompecabezas_play')
def pruebas_locas():
    print(str(session['usuario']) +" - "+str(session['grado']))
    maximo= pinturaC.obtener_maximo_id()
    id = random.randint(1, maximo)
    Rompecabezas = partPuzzleCm.obtenerPartesPintura(id)
    oneArt = pinturaC.obtener_unico_pintura(id)
    presentacion=pinturaC.presentarPintura(id)
    ruta= oneArt[8]
    partes=np.sqrt(presentacion[2])
    pintor=pintorC.obtener_unico_pintor(oneArt[2])[0]
    Estilo=estiloC.ontenerUnicoEstilo(oneArt[4])[0]
    #print(f" Estilo de ruta obtenido = {ruta}")

    
    context={
        'Rompecabezas':Rompecabezas,
        'ruta':ruta,
        'partes':partes,
        'Presentacion':presentacion,
        'Datos':oneArt,
        'Pintor':pintor,
        'Estilo':Estilo
    }
    print(f"el contexto es {context}")
    return render_template('Rompecabezas.html',**context)

@Rompecabezas_Blueprint.route('/loginStudent')
def studentLogin():
    return render_template('loginStudent.html')

@Rompecabezas_Blueprint.route('/Student',  methods=['POST'])
def Student():
    if request.method == 'POST':
        nombre = str(request.form['nombre']).upper()
        grado = str(request.form['grado']).upper()
        if nombre !=None and grado!=None  and nombre != " " and grado != " ":
            session['usuario']=nombre
            session['grado']=grado
            return redirect(url_for('.pruebas_locas'))
        return redirect(url_for('.loginStudent'))

@Rompecabezas_Blueprint.route('/Cuestionario/<string:idPintura>')
def Cuestionario(idPintura):
    usuario=session['usuario']
    grado=session['grado']
    preguntas=preguntaC.obtenerEnunciadoPregunta(idPintura)
    oneArt = pinturaC.obtener_unico_pintura(idPintura)
    presentacion=pinturaC.presentarPintura(idPintura)
    ruta= oneArt[-1]
    #print(f"la ruta es {ruta}")
    respuestas =[]
    for pregunta in preguntas :
        respuestas.append(respuestasC.obtenerRespuestasPregunta(pregunta[0]))


    context={
        'usuario':usuario,
        'grado':grado,
        'pintura':presentacion,
        'ruta':ruta,
        'enunciados':preguntas,
        'respuestas':respuestas
    }
    print(f"el contexto es {context}")
    return render_template('preguntasCuadro.html',**context)
