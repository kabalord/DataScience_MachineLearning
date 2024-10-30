# STRINGS

"""
- Ver documentacion oficial para encontrar todos los métodos
"""

nombreUsuario=input("Introduce tu nombre de usuario : ")
print("El nombre es : ", nombreUsuario.lower())
print("El nombre es : ", nombreUsuario.capitalize())

edad = input("Introduce tu edad : ")
while (edad.isdigit() == False):
    print("Introduce un valor numerico por favor ! ")

    edad = input("Introduce tu edad : ")

if(int(edad)>18):
    print("Puedes pasar")
else:
    print("No puedes pasar")

print(edad.isdigit())

