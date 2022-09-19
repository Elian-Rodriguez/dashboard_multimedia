from flask import Blueprint

Questions_Blueprint = Blueprint('Questions',__name__,template_folder='templates', static_folder='static')

@Questions_Blueprint.route('/Questions')
def pintor():
    return "Pagina Questions"