from flask import Blueprint,request, redirect,render_template,session,flash,url_for
import paintTrimmer as recortador

PuzlePart_Blueprint = Blueprint('PuzlePart',__name__,template_folder='templates', static_folder='static')
@PuzlePart_Blueprint.route('/puzlePart/<string:id_pintura>')
def mostrar_pintura_parte(id_pintura):
    return f"CREACION DE PARTES EXITOSO {id_pintura}"
    pass

@PuzlePart_Blueprint.route('/addPart',methods=['POST'])
def addPart():
    if request.method == 'POST':
        id_pintura=int(request.form['idPintura'])
        numero_total_partes=int(request.form['numero_piezas'])
        ruta_archivo_original=request.form['ruta_interna_server']
        menssanges=str(recortador.recortarRompecabezas(id_pintura,numero_total_partes,ruta_archivo_original))

        try:
            session.pop('_flashes', None)
            session['_flashes'].clear()   
        except Exception as e:
                print(str(e))
        finally:
            flash(menssanges)
            return mostrar_pintura_parte(id_pintura)
        
    return "Pagina PuzlePart"
