from flask import Blueprint,render_template,request,session,flash,redirect,url_for,jsonify,send_file
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage

import controller.pinturaController as pinturaC
import controller.pintorController as pintorC
import controller.continenteController as contineteC
import controller.estiloController as estiloC
from os import getcwd, path, remove


PATH_FILES = getcwd() + "/static/upload/"

Pintura_Blueprint = Blueprint('pintura',__name__,template_folder='templates', static_folder='static')


@Pintura_Blueprint.route('/pintura')
def pintura():
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
def Create_pintura():
    if request.method == 'POST':
        Nombre_pintura=request.form['Nombre_pintura']
        Autor_idAutor=request.form['Autor_idAutor']
        Continente_idContinente=request.form['Continente_idContinente']
        Estilos_pintura_idEstilos_pintura=request.form['Estilos_pintura_idEstilos_pintura']
        year_elaboracion=request.form['year_elaboracion']
        numero_piezas=request.form['numero_piezas']
        Descripcion_pintura=request.form['Descripcion_pintura']
        ruta_interna_server=None
        
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        file_name_generator=str(Nombre_pintura)
        file_name_generator=file_name_generator.replace(" ","_")
        file_name_generator=file_name_generator+"."+str(filename.split(".")[-1])
        file_name_generator=file_name_generator.upper()
        print(str(PATH_FILES))
        f.save(PATH_FILES + file_name_generator)
        ruta_interna_server=str("upload/" + file_name_generator)
        
        print(str(str(type(filename) )+ " " +str(filename) ))
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
            return redirect(url_for('.pintura'))
@Pintura_Blueprint.route('/edit_pintura/<string:id_pintura>')
def editPintura(id_pintura):
    oneArt = pinturaC.obtener_unico_pintura(id_pintura)
    print(str(oneArt))
    menssanges = f"Busqueda de pintor Exitoso {id_pintura}"
    flash(menssanges)
    try:
        session.pop('_flashes', None)
        session['_flashes'].clear()   
    except Exception as e:
            print(str(e))
    finally:
        flash(menssanges)
    return render_template('edit-pintura.html' , oneArt=oneArt)