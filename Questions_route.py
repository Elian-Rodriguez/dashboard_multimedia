from flask import Blueprint,render_template
import controller.preguntaController as preguntasC

Questions_Blueprint = Blueprint('Questions',__name__,template_folder='templates', static_folder='static')

@Questions_Blueprint.route('/Questions')
def Questions():
    Preguntas=preguntasC.preguntasCreadas()

    return render_template('Preguntas.html',Preguntas=Preguntas)