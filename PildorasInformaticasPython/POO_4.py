#POO CONSTRUCTOR

"""
Traslado de codigo los conceptos de POO :
"""

class Coche():
    """
    Propiedades de estado inicial (constructor) :
    Es un método especial que le da estado inicial a los objetos.
    """
    #CONSTRUCTOR : Punto de partida
    def __init__(self):
        self.largoChasis=250
        self.anchoChasis=120
    #ENCAPSULACION : agregar __ para que la variable nos sea accesible desde el exterior
        self.__ruedas=4
        self.enMarcha=False

    def arrancar(self, arrancamos):
        self.enMarcha=arrancamos
        if(self.enMarcha) == True:
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado(self):
        print("EL coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.anchoChasis, " Y un largo de ", self.largoChasis)



miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()


print("----------A continuacion creamos el segundo objeto----------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.ruedas=2
miCoche2.estado()