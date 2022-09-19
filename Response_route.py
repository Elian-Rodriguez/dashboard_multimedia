from flask import Blueprint

Response_Blueprint = Blueprint('response',__name__,template_folder='templates', static_folder='static')

@Response_Blueprint.route('/response')
def pintor():
    return "Pagina Creacion de respuestas"