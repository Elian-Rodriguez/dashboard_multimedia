import cv2
import numpy as np
import controller.partPuzzleController as partPuzzleC
beta=None
def piezas_largo(numero_total_partes):
    return int(np.sqrt(numero_total_partes))

def recortarRompecabezas(id_pintura:int,numero_total_partes:int,ruta_archivo_original:str):
    ruta='./static/'+str(ruta_archivo_original)


    #OBTENER EL NONBRE DE LA PINTURA Y  LA EXTENCION DE LA IMAGEN
    nombre_obra_=ruta.split('/')
    nombre_obra_=str(nombre_obra_[-1])
    nombre_obra_=nombre_obra_.split(".")
    nombre_obra=str(nombre_obra_[0])
    extencion=str(nombre_obra_[1])
    print(f"{extencion}  - {nombre_obra} ")

    # Leemos la imagen de entrada, la mostramos e imprimimos sus dimensiones.
    image = cv2.imread(ruta)
    #Mostramos el grafico en pantalla
    #cv2.imshow('Original', image)
    print(f'Dimensiones de la imagen original: {image.shape[:2]}')
    cv2.waitKey(0)
    #Se obtinen las dimensiones de la imagen 
    Dimensiones=image.shape[:2]
    #SE CALCULA EL LA RAIZ CUADRADA DEL NUMERO TOTAL DE PARTES
    raiz_total_piezas=int(np.sqrt(numero_total_partes))
    #SE OBTINEN UNA TUPLA CON LAS DIMENSIONES DE CADA FICHA
    Dimensiones_partes=tuple(int(i/raiz_total_piezas) for i in Dimensiones)
    print(str(Dimensiones_partes))

    # Como las imágenes en OpenCV no son más que arreglos multidimensionales de NumPy, recortar consiste en escoger
    # un segmento o "slice" de dicho arreglo.
    #


    ancho_total=Dimensiones[1]
    alto_total=Dimensiones[0]

    alto_recorte=(Dimensiones_partes[0])
    ancho_recorte=(Dimensiones_partes[1])
    print(str(alto_recorte), type(alto_recorte))
    print(str(ancho_recorte), type(ancho_recorte))
    #SE DEFINEN ANCHOS DE RECORTE 
    x=0
    y=0
    x1=ancho_recorte
    y1=alto_recorte
    """
    trimHeight
    trimWidth
    """
    #Contador de partes
    parte=1
    #RECORRIDO EN Y
    for i in range (0,raiz_total_piezas):
        #RECORRIDO EN Z
        for o in range (0,raiz_total_piezas):
            cropped = image[y:y1, x:x1]
            #cv2.imshow(f'RECORTE X,Y : ({o} , {i})', cropped)
            nombre_archivo="./static/upload/"+str(nombre_obra)+"_PARTE_"+str(parte)+"."+str(extencion)
            nombre_archivo_a_bd="upload/"+str(nombre_obra)+"_PARTE_"+str(parte)+"."+str(extencion)
            print(str(nombre_archivo))
            cv2.imwrite(nombre_archivo,cropped)
            #print(f'Dimensiones del recorte: {cropped.shape[:2]}')
            #cv2.waitKey(0)
            #print(f"{o} , {i} Dinmensiones ")
            x=x1
            x1=x+ancho_recorte
            partPuzzleC.crearPieza(parte,nombre_archivo_a_bd,id_pintura)
            parte+=1
            print(f"{o},{i} LOS PROXIMOS VALORES SON ({x},{y}) y ({x1},{y1})")
            if x1 > ancho_total or y > alto_total:
                break
        y=y1
        y1=y1+alto_recorte
        x=0
        x1=ancho_recorte
    return f"EXITO GENERANDO RECORTE CON LA PINTURA ID {id_pintura}"

