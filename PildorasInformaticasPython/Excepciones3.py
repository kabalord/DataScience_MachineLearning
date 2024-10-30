# Excepciones
import math
"""
- Lanzamiento de excepciones
    - Instruccion Raise = lanzar excepcion propias
    - Creacion de excepciones propias (POO)
"""


def evaluaEdad(edad):

    if edad < 0:
        raise ZeroDivisionError("No se permiten edades negativas")

    if edad < 20:
        return "Eres muy joven"
    elif edad < 40:
        return "Eres joven"
    elif edad < 65:
        return "Eres maduro"
    elif edad < 100:
        return "Cuidate..."


op3 = (int(input("Introduce tu edad: ")))
print(evaluaEdad(op3))


#use raise

def calculaRaiz(num1):
    if num1 < 0:
        raise ValueError ("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)


op4=(int(input("Introduce un numero para calcular la raiz cuadrada :")))

try:
    print(calculaRaiz(op4))
except ValueError as ErrorDeNumeroNegativo:
    print(ErrorDeNumeroNegativo)

print("El programa a finalizado")

