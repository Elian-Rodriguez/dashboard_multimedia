from flask import Blueprint,flash,render_template,redirect,request,session,url_for
import controller.estiloController as estiloc

Estilo_Blueprint = Blueprint('estiloPinura',__name__,template_folder='templates', static_folder='static')


@Estilo_Blueprint.route('/estiloPintura')
def estiloPinura():
    Estilos=estiloc.obtenerVisualEstilo()
    return render_template('Estilo.html',Estilos=Estilos)

@Estilo_Blueprint.route('/addPaintingStyle' , methods=['POST'])
def Crear_estilo():
    if request.method == 'POST':
        Nombre_estilo = request.form['Nombre_estilo']
        Descripcion_Estilo = request.form['Descripcion_Estilo']
        menssanges=str(estiloc.crearEstilo(Nombre_estilo,Descripcion_Estilo))
        try:
            session.pop('_flashes', None)
            session['_flashes'].clear()   
        except Exception as e:
                print(str(e))
        finally:
            flash(menssanges)
            return redirect(url_for('.estiloPinura'))

@Estilo_Blueprint.route('/editPaintingStyle/<string:idEstilos_pintura>', methods=['POST','GET'])
def getEstilo(idEstilos_pintura):
    print("CONTINENTE UNICO ID UNICO")
    data = estiloc.ontenerUnicoEstilo(idEstilos_pintura)
    print(data[0])
    menssanges = f"Busqueda de Estilo de pintura Exitoso {idEstilos_pintura}"
    flash(menssanges)
    try:
        session.pop('_flashes', None)
        session['_flashes'].clear()   
    except Exception as e:
            print(str(e))
    finally:
        flash(menssanges)
        return render_template('editPaintingStyle.html', Onestyle=data[0])


@Estilo_Blueprint.route('/updatePaintingStyle/<string:Onestyle>', methods=['POST'])
def update_Estilo(Onestyle):
    if request.method == 'POST':
        Nombre_estilo = request.form['Nombre_estilo']
        id = request.form['idEstilos_pintura']
        Descripcion_Estilo = request.form['Descripcion_Estilo']
        menssanges=str(estiloc.actualizarEstilo(Nombre_estilo,Descripcion_Estilo,id))
        try:
            session.pop('_flashes', None)
            session['_flashes'].clear()   
        except Exception as e:
                print(str(e))
        finally:
            flash(menssanges)
            return redirect(url_for('.estiloPinura'))

@Estilo_Blueprint.route('/deletePaintingStyle/<string:id_continente>')
def inactivar_Estilo(id_continente):
    menssanges = estiloc.eliminarEstilo(id_continente)
    try:
        session.pop('_flashes', None)
        session['_flashes'].clear()   
    except Exception as e:
            print(str(e))
    finally:
        flash(menssanges)
        return redirect(url_for('.estiloPinura'))