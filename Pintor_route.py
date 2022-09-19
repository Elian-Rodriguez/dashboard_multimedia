from flask import Blueprint,render_template
import controller.pintorController as pintorC

pintor_Blueprint = Blueprint('pintor',__name__,template_folder='templates', static_folder='static')



@pintor_Blueprint.route('/pintor')
def pintor():
    Pintores=pintorC.obtener_pintor_visual()
    return render_template('Pintor.html',Pintores=Pintores)