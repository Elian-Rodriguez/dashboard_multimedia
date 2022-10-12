import controller.partPuzzleController as partPuzzleCm
import controller.pinturaController as pinturaC
import controller.pintorController as pintorC
import controller.estiloController as estiloC
from flask import Blueprint,render_template
import random
import numpy as np

Rompecabezas_Blueprint = Blueprint('Rompecabezas',__name__,template_folder='templates', static_folder='static')


@Rompecabezas_Blueprint.route('/Rompecabezas_play')
def pruebas_locas():
    maximo= pinturaC.obtener_maximo_id()
    id = random.randint(1, maximo)
    Rompecabezas = partPuzzleCm.obtenerPartesPintura(id)
    oneArt = pinturaC.obtener_unico_pintura(id)
    presentacion=pinturaC.presentarPintura(id)
    ruta= oneArt[8]
    partes=np.sqrt(presentacion[2])
    pintor=pintorC.obtener_unico_pintor(oneArt[2])[0]
    Estilo=estiloC.ontenerUnicoEstilo(oneArt[4])[0]
    print(f" Estilo de pintura obtenido = {Estilo}")

    
    context={
        'Rompecabezas':Rompecabezas,
        'ruta':ruta,
        'partes':partes,
        'Presentacion':presentacion,
        'Datos':oneArt,
        'Pintor':pintor,
        'Estilo':Estilo
    }
    return render_template('Rompecabezas.html',**context)