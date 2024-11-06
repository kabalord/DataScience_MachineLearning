# SERIALIZACION

"""
- Serializacion de objetos.

"""
import pickle
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




coche1=Vehiculo("Mazda", "MX5")
coche2=Vehiculo("Seat", "Leon")
coche3=Vehiculo("Renault", "Megane")

coches=[coche1, coche2, coche3]


fichero=open("losCoches","wb")

pickle.dump(coches, fichero)

fichero.close()

del(fichero)


#rescatar la informacion del fichero
fichero_apertura=open("losCoches", "rb")

#crear una variable en donde volcar la informacion del fichero
misCoches=pickle.load(fichero_apertura)

fichero_apertura.close()

#recorrer la informacion del fichero
for c in misCoches:
    print(c.estado())
