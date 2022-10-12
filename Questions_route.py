from flask import Blueprint,render_template,request,session,flash,url_for,redirect
import controller.preguntaController as preguntasC
import controller.pinturaController as pinturaC
import controller.respuestaController as respuestaC

Questions_Blueprint = Blueprint('Questions',__name__,template_folder='templates', static_folder='static')

@Questions_Blueprint.route('/Questions')
def Questions():
    Preguntas=preguntasC.preguntasCreadas()
    pinturas = pinturaC.listar_pinturas()
    
    context={
        'Preguntas':Preguntas,
        'Pinturas':pinturas
        }

    return render_template('Preguntas.html',**context)
@Questions_Blueprint.route('/addPregunta',methods=['POST'])
def crearPregunta():
    if request.method == 'POST':
        Enunciado = request.form['ENUNCIADO'] 
        id_pintura= int(request.form['Pintura'])
        if  Enunciado!=None and  id_pintura !=None and id_pintura >0:
            menssanges=str(preguntasC.crearPregunta(Enunciado,id_pintura))
        try:
            session.pop('_flashes', None)
            session['_flashes'].clear()   
        except Exception as e:
                print(str(e))
        finally:
            flash(menssanges)
            return redirect(url_for('.Questions'))

@Questions_Blueprint.route('/editPregunta/<string:id_pregunta>')
def obtenerPregunta(id_pregunta):
    print(id_pregunta)
    Pregunta=preguntasC.obtenerUnicaPreguntaDescripcion(id_pregunta)
    Respuestas=respuestaC.obtenerRespuestasPregunta(id_pregunta)
    print(str(Respuestas))
    context={
        'Pregunta':Pregunta,
        'Respuestas':Respuestas
    }
    return render_template('Pregunta_respuesta.html',**context)