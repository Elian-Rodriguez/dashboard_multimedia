from flask import Blueprint,render_template,request,session,flash,redirect,url_for
import controller.pinturaController as pinturaC
import controller.pintorController as pintorC
import controller.continenteController as contineteC
import controller.estiloController as estiloC
Pintura_Blueprint = Blueprint('pintura',__name__,template_folder='templates', static_folder='static')

@Pintura_Blueprint.route('/pintura')
def pinturas():
    pinturas = pinturaC.listar_pinturas()
    pintores = pintorC.obtener_pintor_visual()
    Continentes = contineteC.obtenerContinente()
    Estilos = estiloC.obtenerVisualEstilo()
    
    context ={
        'pinturas':pinturas,
        'pintores':pintores,
        'Continentes':Continentes,
        'Estilos':Estilos
    }
    return render_template('Pintura.html',**context)


@Pintura_Blueprint.route('/add_pintura' , methods=['POST'])
def Create_pintor():
    if request.method == 'POST':
        Nombre_pintura:request.form['Nombre_pintura']
        Autor_idAutor=None
        Continente_idContinente=None
        Estilos_pintura_idEstilos_pintura=None
        year_elaboracion=None
        numero_piezas=None
        Descripcion_pintura:request.form['Nombre_pintura']
        ruta_interna_server=None

        menssanges=str(pinturaC.Crear_pintura(Nombre_pintura,
                Autor_idAutor,
                Continente_idContinente,
                Estilos_pintura_idEstilos_pintura,
                year_elaboracion,
                numero_piezas,
                Descripcion_pintura,
                ruta_interna_server))
        try:
            session.pop('_flashes', None)
            session['_flashes'].clear()   
        except Exception as e:
                print(str(e))
        finally:
            flash(menssanges)
            return redirect(url_for('.pintor'))
        