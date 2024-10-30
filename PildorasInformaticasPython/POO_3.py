#POO

'''
Los objetos tienen :
    - Estado
    - Propiedades
    - Comportamiento

Sintaxis :

class Coche():
    """
    definir propiedades :
    """
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enMarcha=False

    """
    definir un comportamiento :
     - a traves de los métodos
    """

    def arrancar(self):
        """
        el mismo this (Java o C++)
        en python es el primer parametro obligatorio
         self : hace referencia a el propio objeto perteneciente a la clase
         hace referencia a la instancia perteneciente a la clase
        """
        pass
    """
    Si la funcion esta vacia pass asegura que no haya fallo
    """

"""
Como construir la primera instancia 
    - darle nombre
    - nombre de la clase
"""

#instanciar la clase
miCoche=Coche()

#para acceder a las propiedades del objeto usar la nomenclatura del punto
print("El largo del coche es : ", miCoche.largoChasis)
print("El coche tiene : ", miCoche.ruedas, "Ruedas")
'''

class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enMarcha=False

    def arrancar(self):
        self.enMarcha=True

    def estado(self):
        if(self.enMarcha) == True:
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"



miCoche=Coche()
print("El largo del coche es : ", miCoche.largoChasis)
print("El coche tiene : ", miCoche.ruedas, "Ruedas")
miCoche.arrancar()
print(miCoche.estado())



