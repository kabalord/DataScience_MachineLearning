# Excepciones

"""
Que son ?
Las excepciones son errores que ocurren
durante la ejecucion de un programa.
La sintaxis del codigo es correcta
pero durante la ejecucion a ocurrido
'algo inesperado'.

para solucionar este problema hay que hacer :
una captura o control de excepcion.
"""


def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):

    try:
        return num1 / num2
    except:ZeroDivisionError:\
        print("No se puede dividir entre 0")
    return "operacion no valida"


op1 = (int(input("Introduce el primer número: ")))

op2 = (int(input("Introduce el segundo número: ")))

operacion = input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion == "suma":
    print(suma(op1, op2))

elif operacion == "resta":
    print(resta(op1, op2))

elif operacion == "multiplica":
    print(multiplica(op1, op2))

elif operacion == "divide":
    print(divide(op1, op2))

else:
    print("Operación no contemplada")

print("Operación ejecutada. Continuación de ejecúción del programa ")


