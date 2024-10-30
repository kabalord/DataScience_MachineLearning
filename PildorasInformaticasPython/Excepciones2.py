# Excepciones

"""
- Captura de varias excepciones
- Clausula finally

"""
def divide():
    try:
        op1=(float(input("Introduce el primer numero :")))
        op2=(float(input("Introduce el primer numero :")))

        print("La division es: " + str(op1/op2))

    except ValueError:
        print("El valor introducido es erroneo")
    except ZeroDivisionError:
        print("No se pude dividir entre 0!")
    finally:
        print("Calculo finalizado")

divide()


# use while and break

def suma(num1, num2):
    return num1 + num2


def resta(num1, num2):
    return num1 - num2


def multiplica(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1 / num2
    except:
        ZeroDivisionError: \
            print("No se puede dividir entre 0")
    return "operacion no valida"


while True:
    try:

        op1 = (int(input("Introduce el primer número: ")))

        op2 = (int(input("Introduce el segundo número: ")))

        break

    except ValueError:
        print("Los valores introducidos no son correctos. Intentalo de nuevo.")

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





