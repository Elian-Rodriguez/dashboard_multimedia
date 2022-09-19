from flask import Blueprint

Pintura_Blueprint = Blueprint('pintura',__name__,template_folder='templates', static_folder='static')

@Pintura_Blueprint.route('/pintura')
def pintor():
    return "Pagina Pintura"