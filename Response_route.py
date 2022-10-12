from flask import Blueprint,request,session,render_template,flash,redirect,url_for
from controller import respuestaController  as respuestaC
import Questions_route as ruta_pregunta
Response_Blueprint = Blueprint('response',__name__,template_folder='templates', static_folder='static')

@Response_Blueprint.route('/response')
def pintor():
    return "Pagina Creacion de respuestas"

@Response_Blueprint.route('/addRespuesta',methods=['POST'])
def crearRespuesta():
    if request.method == 'POST':
        respuesta = (request.form['respuesta_var']).upper() 
        id_pregunta= int(request.form['questions_idquestions'])
        es_correcto= int(request.form['Es_correcta'])
        if  respuesta!=None and  id_pregunta !=None and es_correcto !=None:
            menssanges=str(respuestaC.crearRespuesta(respuesta,es_correcto,id_pregunta))
        try:
            session.pop('_flashes', None)
            session['_flashes'].clear()   
        except Exception as e:
                print(str(e))
        finally:
            flash(menssanges)
            direccion=f"editPregunta/{id_pregunta}"
            direccion=f"Questions.Question"
            return ruta_pregunta.obtenerPregunta(id_pregunta)

