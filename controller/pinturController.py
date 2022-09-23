
import base64
from os import system
from sqlite3 import dbapi2
from unicodedata import name
from Data_connection import obtener_conexion 
#from controller.Data_connection import obtener_conexion 
import sys #importar metodos del systema
import base64
from PIL import Image
import io 

def crearPintura():
    nombre_pintura="MONALISA"
    id_pintor=4
    id_continente=4
    id_estilo=3
    year_creacion=1503
    numero_piezas=9
    descripcion_imagen="En este retrato la dama está sentada en un sillón y posa sus brazos en los brazos del asiento. En sus manos y sus ojos puede verse un ejemplo característico del dolor y del juego que el pintor hace con la luz y la sombra para dar sensación de volumen"

    # Create a cursor object
    conexion = obtener_conexion()
    cursor = conexion.cursor() 
    
    # Open a file in binary mode
    file = open('monalisa.jpg','rb').read()
    
    # We must encode the file to get base64 string
    file = base64.b64encode(file)
    
    # Sample data to be inserted
    args = (nombre_pintura, id_pintor, id_continente,id_estilo,year_creacion,numero_piezas, file,descripcion_imagen)
    
    # Prepare a query
    query = 'INSERT INTO PROFILE VALUES(%s, %s, %s)'
    query="""INSERT INTO bosdos6qw6vefrichu88.Pintura
    ( Nombre_pintura, Autor_idAutor, Continente_idContinente, Estilos_pintura_idEstilos_pintura, year_elaboracion, numero_piezas, pintura_img, Descripcion_pintura)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s);

    """
    
    # Execute the query and commit the database.
    cursor.execute(query,args)
    conexion.commit()
    conexion.close()

def obtenerPintura():
    # Create a cursor object
    conexion = obtener_conexion()
    cursor = conexion.cursor() 
    
    # Prepare the query obtener la imagen
    query = 'SELECT pintura_img FROM bosdos6qw6vefrichu88.Pintura WHERE idPintura=1'
    # Execute the query to get the file
    cursor.execute(query)
    data = cursor.fetchall()
    
    # The returned data will be a list of list
    image = data[0][0]

    query = """SELECT p.idPintura , p.Nombre_pintura ,p.numero_piezas ,p.Descripcion_pintura ,
                a.Nombre_autor ,a.Apellido ,p.year_elaboracion ,ep.Nombre_estilo 
                FROM  bosdos6qw6vefrichu88.Pintura p 
                inner join bosdos6qw6vefrichu88.Autor a on(p.Autor_idAutor=a.idAutor)
                inner join bosdos6qw6vefrichu88.Estilos_pintura ep on (p.Estilos_pintura_idEstilos_pintura=ep.idEstilos_pintura)
                WHERE  p.idPintura =1;"""
    # Execute the query to get the file
    cursor.execute(query)
    data_description = cursor.fetchone()
    nombre_archivo= str(data_description[1])
    nombre_archivo=str(nombre_archivo.replace(" ","_")+"_FONDO")

    Descripcion_rompecabezas =f"{data_description[1]}\nElaborada por {data_description[4]}  {data_description[5]} en el año {data_description[6]} , bajo el estilo de pintura {data_description[7]}. \n{data_description[3]}. \nEl rompecabezad tiene {data_description[2]}"
    
    # Decode the string
    binary_data = base64.b64decode(image)
    
    # Convert the bytes into a PIL image

    image = Image.open(io.BytesIO(binary_data))
    print(str(Descripcion_rompecabezas))
    # Display the image
    nombre_archivo=str(nombre_archivo)+"."+image.format
    image.save(nombre_archivo)
    #image.show()

obtenerPintura()