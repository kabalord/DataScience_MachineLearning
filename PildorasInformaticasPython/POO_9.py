# POO POLIMORFISMO

"""
- Que es ?
    - un objeto puede cambiar de forma dependiendo del contexto que se utilize
    y por lo tanto el comportamiento tambien cambia

"""

class Coche():

    def desplazamiento(self):
        print("Me desplazo utilisando cuatro ruedas")


class Moto():

    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")

class Camion():

    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas ")

# Para aplicar el polimorfismo podemos crear una funcion de la siguiente manera :
def desplazamiento_vehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo=Moto()

desplazamiento_vehiculo(miVehiculo)