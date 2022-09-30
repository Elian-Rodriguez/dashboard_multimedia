import controller.partPuzzleController as partPuzzleCm
import controller.pinturaController as pinturaC
import controller.pintorController as pintorC
from flask import Blueprint,render_template
import random
import numpy as np

Rompecabezas_Blueprint = Blueprint('Rompecabezas',__name__,template_folder='templates', static_folder='static')

@Rompecabezas_Blueprint.route('/Questions')
def pintor():
    return "Pagina Questions"

@Rompecabezas_Blueprint.route('/Rompecabezas_play')
def pruebas_locas():
    id = random.randint(1, 2)
    Rompecabezas = partPuzzleCm.obtenerPartesPintura(id)
    oneArt = pinturaC.obtener_unico_pintura(id)
    presentacion=pinturaC.presentarPintura(id)
    ruta= oneArt[8]
    partes=np.sqrt(presentacion[2])
    print(str(presentacion))
    
    context={
        'Rompecabezas':Rompecabezas,
        'ruta':ruta,
        'partes':partes,
        'Presentacion':presentacion,
        'Datos':oneArt
    }
    return render_template('Rompecabezas.html',**context)