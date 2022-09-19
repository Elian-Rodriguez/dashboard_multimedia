from flask import Blueprint

Continente_Blueprint = Blueprint('Continente',__name__,template_folder='templates', static_folder='static')

@Continente_Blueprint.route('/Continente')
def pintor():
    return "Pagina Continete"