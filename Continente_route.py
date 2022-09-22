from flask import Blueprint,render_template,request,session,flash,redirect,url_for
import controller.continenteController as continetec

Continente_Blueprint = Blueprint('Continente',__name__,template_folder='templates', static_folder='static')

@Continente_Blueprint.route('/Continente')
def Continente():
    Continentes=continetec.obtenerVisualContinente()
    return render_template('Continente.html',Continentes=Continentes)

@Continente_Blueprint.route('/addContinet' , methods=['POST'])
def crearContinente():
    if request.method == 'POST':
        Nombre_continente = request.form['Nombre_continente']
        menssanges=str(continetec.crearContinentw(Nombre_continente))
        try:
            session.pop('_flashes', None)
            session['_flashes'].clear()   
        except Exception as e:
                print(str(e))
        finally:
            flash(menssanges)
            return redirect(url_for('.Continente'))

@Continente_Blueprint.route('/editContinet/<string:id_continente>')
def getContinent(id_continente):
    print("CONTINENTE UNICO ID UNICO")
    data = continetec.ontenerUnicoContinente(id_continente)
    print(data[0])
    menssanges = f"Busqueda de Continente Exitoso {id_continente}"
    flash(menssanges)
    try:
        session.pop('_flashes', None)
        session['_flashes'].clear()   
    except Exception as e:
            print(str(e))
    finally:
        flash(menssanges)
        return render_template('edit-continent.html', Onecontinent=data[0])


@Continente_Blueprint.route('/updateContinente/<string:Onecontinent>', methods=['POST'])
def update_pintor(Onecontinent):
    if request.method == 'POST':
        Nombre_continente = request.form['Nombre_continente']
        id = request.form['idContinente']
        menssanges=str(continetec.actualizarContinente(Nombre_continente,id))
        try:
            session.pop('_flashes', None)
            session['_flashes'].clear()   
        except Exception as e:
                print(str(e))
        finally:
            flash(menssanges)
            return redirect(url_for('.Continente'))

@Continente_Blueprint.route('/deleteContinet/<string:id_continente>')
def inactivar_pintor(id_continente):
    menssanges = continetec.eliminarContinente(id_continente)
    try:
        session.pop('_flashes', None)
        session['_flashes'].clear()   
    except Exception as e:
            print(str(e))
    finally:
        flash(menssanges)
        return redirect(url_for('.Continente'))