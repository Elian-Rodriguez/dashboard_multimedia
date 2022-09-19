from flask import Blueprint

Estilo_Blueprint = Blueprint('estiloPinura',__name__,template_folder='templates', static_folder='static')

@Estilo_Blueprint.route('/estiloPintura')
def pintor():
    return "Pagina Estilo pintura"