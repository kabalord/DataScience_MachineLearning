#POO ENCAPSULACION

"""
- Encapsulacion de métodos
    - que es ?
        -es para que solo sea accesible desde dentro de la clase
    - porque utilizar la encapsulacion ?
     - cuando el objeto asi lo necesite y eso depende del comportamiento
    ségun el criterio del programador quiere que funcione su clase y objetos
"""

class Coche():

    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enMarcha=False

    def arrancar(self, arrancamos):
        self.__enMarcha=arrancamos

        if(self.__enMarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enMarcha and chequeo):
            return "El coche esta en marcha"

        elif(self.__enMarcha and chequeo==False):
            return "Algo va mal en el chequeo, no se puede arrancar"
        else:
            return "El coche esta parado"

    def estado(self):
        print("EL coche tiene ", self.__ruedas, " ruedas. Un ancho de ", self.__anchoChasis, " Y un largo de ", self.__largoChasis)


    #ENCAPSULAR UN METODO : agregar __ en el metodo y en donde se utiliza también
    def __chequeo_interno(self):
        print("realizando chequeo interno")

        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas") :
            return True
        else:
            return False



miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()


print("----------A continuacion creamos el segundo objeto----------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()