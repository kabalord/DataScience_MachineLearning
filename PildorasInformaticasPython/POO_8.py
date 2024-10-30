#POO HERENCIA MULTIPLE

"""
- Herencia
    - super()
    - isinstance() : Principio de sustitucion
"""

class Persona():

    def __init__(self, nombre, edad, residencia):

        self.nombre=nombre
        self.edad=edad
        self.residencia=residencia



    def descripcion(self):

        print("Nombre:",self.nombre, "Edad:",self.edad, "Residencia:",self.residencia)

# La funcion super() llama el constructor de la clase padre para agregar los parametros faltantes
class Empleado(Persona):

    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario=salario
        self.antiguedad=antiguedad

    # La funcion super().descripcion() para completar todos los parametros de las dos clases
    def descripcion(self):

        super().descripcion()

        print("Salario:", self.salario, "Antiguedad:", self.antiguedad)

Walter=Empleado(1500, 3, "Walter", 38, "Colombia")

Walter.descripcion()

# Utilizacion de isinstance()
"""
PRINCIPIO DE SUBSTITUCION :

Una subclase siempre sera un objeto de la superclase
un Empleado siempre es Persona
pero :
Una Persona no siempre es empleado

isinstance(): comprobar si un objeto es instancia de una clase
"""

print(isinstance(Walter, Persona))

Diana=Persona("Diana", 34, "Colombia")
print(isinstance(Diana, Empleado))