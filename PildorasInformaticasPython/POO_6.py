#POO HERENCIA

"""
- Que es la herencia ?
    -Se trata de trasladar el comportamiento de la clase padre (superclase)
      a los hijos(subclases)

- Para que sirve ?
    -para reutilizar codigo en caso de crear objetos similares
        - marca
        - modelo

    - que caracteristicas en comun tienen todos los objetos
    - que comportamientos en comun tienen todos los objetos
        - arrancan
        - aceleran
        - frenan

- Como hacer que las clases hereden

    -hay que englobar en una superclase

"""

class Vehiculo():

    def __init__(self, marca, modelo):

        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar(self):

        self.enmarcha=True

    def acelera(self):

        self.acelera=True

    def frena(self):

        self.frena=True

    def estado(self):

        print("\n Marca : ", self.marca,
              "\n Modelo : ", self.modelo,
              "\n En marche : ", self.enmarcha,
              "\n Acelerando : ", self.acelera,
              "\n Frenando : ", self.frena)



miCoche=Vehiculo("renault", "megane")
miCoche.estado()

# Para heredar solo basta con pasar la superclase(padre) como parametro de la subclase(hijo)
class Moto(Vehiculo):
    pass

miMoto=Moto("honda", "cbr")
miMoto.estado()