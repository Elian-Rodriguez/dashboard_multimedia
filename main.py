from flask import Flask,render_template,request,flash,url_for,redirect,session
from flask_login import login_manager,login_user,logout_user,login_required
from config import Config
from Pintor_route import pintor_Blueprint
from Continente_route import Continente_Blueprint
from Pintura_route import Pintura_Blueprint
from Response_route import Response_Blueprint
from Estilo_route import Estilo_Blueprint
from Questions_route import Questions_Blueprint
from FieldMultimedia_route import FieldMultimedia_Blueprint
from PuzlePart_route import PuzlePart_Blueprint
from Rompecabezas_route import Rompecabezas_Blueprint



app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(pintor_Blueprint)
app.register_blueprint(Continente_Blueprint)
app.register_blueprint(Response_Blueprint)
app.register_blueprint(Pintura_Blueprint)
app.register_blueprint(Estilo_Blueprint)
app.register_blueprint(Questions_Blueprint)
app.register_blueprint(FieldMultimedia_Blueprint)
app.register_blueprint(PuzlePart_Blueprint)
app.register_blueprint(Rompecabezas_Blueprint)

app.secret_key = "mysecretkey"


@app.route('/')
def index():
    return render_template('login.html')



@app.route('/index_admin',  methods=['POST'])
def index_admin():
    if request.method == 'POST':
        usuario = request.form['user']
        password = request.form['pass']
        if (usuario == "Homero" and password == "Linux-2022"):
            menssanges = 'Ingreso Autorizado'
            flash(menssanges)
            return render_template('dashboard.html')
        else:
            try:
                session['_flashes'].clear()
                session.pop('_flashes', None)
            except Exception as e:
                print(str(e))
            finally:
                menssanges = 'Ingreso Incorrecto, Intente Nuevamente'
                flash(menssanges)
                return index()
    else:
        try:
            session['_flashes'].clear()
            session.pop('_flashes', None)
        except Exception as e:
            print(str(e))
        finally:
            return index() 

@app.errorhandler(400)
def access_error(error):
    return render_template('500.html'), 400
@app.errorhandler(401)
def access_error(error):
    return render_template('500.html'), 401
@app.errorhandler(404)
def access_error(error):
    return render_template('500.html'), 404

@app.errorhandler(500)
def access_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=False,port=5000, host="0.0.0.0")
    #app.run(debug=True)
