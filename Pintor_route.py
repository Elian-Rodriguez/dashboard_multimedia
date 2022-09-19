from flask import Blueprint,render_template,request,flash,session,redirect,url_for
import controller.pintorController as pintorC

pintor_Blueprint = Blueprint('pintor',__name__,template_folder='templates', static_folder='static')



@pintor_Blueprint.route('/pintor')
def pintor():
    Pintores=pintorC.obtener_pintor_visual()
    return render_template('Pintor.html',Pintores=Pintores)

@pintor_Blueprint.route('/add_pintor' , methods=['POST'])
def Create_pintor():
    if request.method == 'POST':
        Nombre_autor = request.form['Nombre_autor']
        Apellido_autor = request.form['Apellido_autor']
        Biografia = request.form['Biografia']

        menssanges=str(pintorC.Crear_pintor(Nombre_autor,Apellido_autor,Biografia))
        try:
            session.pop('_flashes', None)
            session['_flashes'].clear()   
        except Exception as e:
                print(str(e))
        finally:
            flash(menssanges)
            return redirect(url_for('.pintor'))
        
@pintor_Blueprint.route('/edit_pintor/<string:id_pintor>')
def get_pintor(id_pintor):
    print("PINTOR ID UNICO")
    data = pintorC.obtener_unico_pintor(id_pintor)
    print(data[0])
    menssanges = f"Busqueda de pintor Exitoso {id_pintor}"
    flash(menssanges)
    try:
        session.pop('_flashes', None)
        session['_flashes'].clear()   
    except Exception as e:
            print(str(e))
    finally:
        flash(menssanges)
        return render_template('edit-pintor.html', Onepintur=data[0])


@pintor_Blueprint.route('/update_pintor/<string:Onepintur>', methods=['POST'])
def update_pintor(Onepintur):
    if request.method == 'POST':
        Nombre_autor = request.form['Nombre_autor']
        Apellido_autor = request.form['Apellido_autor']
        Biografia = request.form['Biografia']
        id_autor= request.form['idAutor']
        menssanges=str(pintorC.actualizar_pintor(Nombre_autor,Apellido_autor,Biografia,id_autor))
        try:
            session.pop('_flashes', None)
            session['_flashes'].clear()   
        except Exception as e:
                print(str(e))
        finally:
            flash(menssanges)
            return redirect(url_for('.pintor'))

@pintor_Blueprint.route('/delete_pintor/<string:id_pintor>')
def inactivar_pintor(id_pintor):
    menssanges = pintorC.actualizar_visualizacion(id_pintor)
    try:
        session.pop('_flashes', None)
        session['_flashes'].clear()   
    except Exception as e:
            print(str(e))
    finally:
        flash(menssanges)
        return redirect(url_for('.pintor'))
