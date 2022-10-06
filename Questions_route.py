from flask import Blueprint,render_template,request,session,flash,url_for,redirect
import controller.preguntaController as preguntasC
import controller.pinturaController as pinturaC

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