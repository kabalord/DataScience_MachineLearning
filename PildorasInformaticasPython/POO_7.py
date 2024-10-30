#POO HERENCIA MULTIPLE

"""
- Sobre escritura de métodos
- herencia simple y multiple
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



miCoche=Vehiculo("Renault", "MEGANE")
miCoche.estado()

# Para heredar solo basta con pasar la superclase(padre) como parametro de la subclase(hijo)
class Moto(Vehiculo):
    hcaballito=""
    def caballito(self):
        self.hcaballito="Voy haciendo el caballito"


    def estado(self):
        print("\n Marca : ", self.marca,
              "\n Modelo : ", self.modelo,
              "\n En marche : ", self.enmarcha,
              "\n Acelerando : ", self.acelera,
              "\n Frenando : ", self.frena,
              "\n Caballito :", self.hcaballito)



miMoto=Moto("Honda", "CBR")
miMoto.caballito()
miMoto.estado()

class Furgoneta(Vehiculo):

    def carga(self, cargar):
        self.cargado=cargar

        if(self.cargado)==True:
            return "\n La furgoneta esta cargada"
        else:
            return "\nLa furgoneta no esta cargada"

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

class VElectrico(Vehiculo):

    def __init__(self, marca, modelo):
    # Para poder agregar la marca y el modelo
        super().__init__(marca, modelo)

        self.autonomia=100

    def cargarEnergia(self):

        self.cargando=True

#En la herencia multiple se le da prioridad al orden de las clases heredadas en los parametros
class BicicletaElectrica(VElectrico,Vehiculo):
    pass

miBici=BicicletaElectrica("Orbeo", "HC1030")
miBici.estado()