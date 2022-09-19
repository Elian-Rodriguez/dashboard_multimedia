from flask import Blueprint

FieldMultimedia_Blueprint = Blueprint('FieldMultimedia',__name__,template_folder='templates', static_folder='static')

@FieldMultimedia_Blueprint.route('/FieldMultimedia')
def pintor():
    return "Pagina FieldMultimedia"