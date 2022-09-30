import controller.partPuzzleController as partPuzzleCm
import controller.pinturaController as pinturaC
from flask import Blueprint,render_template
import random

Rompecabezas_Blueprint = Blueprint('Rompecabezas',__name__,template_folder='templates', static_folder='static')

@Rompecabezas_Blueprint.route('/Questions')
def pintor():
    return "Pagina Questions"

@Rompecabezas_Blueprint.route('/pruebas_locas')
def pruebas_locas():
    id = random.randint(1, 2)
    Rompecabezas = partPuzzleCm.obtenerPartesPintura(id)
    oneArt = pinturaC.obtener_unico_pintura(id)
    ruta= oneArt[8]
    #ruta=" url_for('static', filename= '"+str(ruta)+"')"
    return render_template('pruebas_locas.html',Rompecabezas=Rompecabezas,ruta=ruta)