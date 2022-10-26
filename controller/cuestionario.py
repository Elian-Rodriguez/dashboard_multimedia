import pinturaController as pinturaC
import preguntaController as preguntaC
class Pregunta:
    def __init__(self,idPregunta):
        pass


class  Cuestionario:
    def __init__(self,idPintura):
        pintura=pinturaC.obtener_unico_pintura(idPintura)
        self.idPintura=pintura[0]
        self.nombrePintura=pintura[1]
        self.preguntas=preguntaC.obtenerEnunciadoPregunta(idPintura)


        pass