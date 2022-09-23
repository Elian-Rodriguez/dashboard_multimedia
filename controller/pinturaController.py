from controller.Data_connection import obtener_conexion 

def Crear_pintura(Nombre_pintura:str,
                Autor_idAutor:str,
                Continente_idContinente:str,
                Estilos_pintura_idEstilos_pintura:str,
                year_elaboracion:str,
                numero_piezas:str,
                Descripcion_pintura:str,
                ruta_interna_server):
    Nombre_pintura=Nombre_pintura.upper()
    Apellido=Apellido.upper()
    conexion = obtener_conexion()
    Consulta =f"""INSERT INTO bosdos6qw6vefrichu88.Pintura
		(Nombre_pintura, Autor_idAutor, Continente_idContinente, Estilos_pintura_idEstilos_pintura, year_elaboracion, numero_piezas, Descripcion_pintura, ruta_interna_server)
		VALUES('{Nombre_pintura}', {Autor_idAutor}, {Continente_idContinente}, {Estilos_pintura_idEstilos_pintura}, {year_elaboracion}, {numero_piezas},'{Descripcion_pintura}', {ruta_interna_server});"""
    with conexion.cursor() as cursor:
        cursor.execute(Consulta)
    conexion.commit()
    conexion.close()
    return str(f"SE GENERO CORRECTAMENTE EL INSERT DE {Nombre_pintura}")

def listar_pinturas():
    conexion = obtener_conexion()
    pinturas = []
    with conexion.cursor() as cursor:
        cursor.execute("""SELECT p.idPintura , p.Nombre_pintura ,p.numero_piezas  ,
                CONCAT( a.Nombre_autor,' ',a.Apellido) as Nombre_autor ,p.year_elaboracion ,ep.Nombre_estilo,c.Nombre_continente 
                FROM  bosdos6qw6vefrichu88.Pintura p 
                inner join bosdos6qw6vefrichu88.Autor a on(p.Autor_idAutor=a.idAutor)
                inner join bosdos6qw6vefrichu88.Estilos_pintura ep on (p.Estilos_pintura_idEstilos_pintura=ep.idEstilos_pintura)
                inner JOIN bosdos6qw6vefrichu88.Continente c on(p.Continente_idContinente=c.idContinente)""")
        pinturas = cursor.fetchall()
    conexion.close()
    return pinturas

def obtener_unico_pintura(id):
    conexion = obtener_conexion()
    pintura = []
    with conexion.cursor() as cursor:
        cursor.execute(f"""SELECT idPintura, Nombre_pintura, Autor_idAutor, Continente_idContinente, Estilos_pintura_idEstilos_pintura, year_elaboracion, numero_piezas, Descripcion_pintura, ruta_interna_server
                            FROM bosdos6qw6vefrichu88.Pintura
                            WHERE idPintura={id}; """)
        pintura = cursor.fetchall()
    conexion.close()
    print(str(pintura))
    return pintura


