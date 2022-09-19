from flask import Blueprint

PuzlePart_Blueprint = Blueprint('PuzlePart',__name__,template_folder='templates', static_folder='static')

@PuzlePart_Blueprint.route('/PuzlePart')
def pintor():
    return "Pagina PuzlePart"