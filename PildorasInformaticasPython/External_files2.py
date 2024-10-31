# ARCHIVOS EXTERNOS

"""
- Modificar la posicion del puntero
    - usar seek()
"""

from io import open

archivo_texto=open("archivo.txt", "r")

archivo_texto.seek(28)
print(archivo_texto.read())
archivo_texto.seek(0)
print(archivo_texto.read())

#para imprimir hasta un una posicion a partir de donde se encuentra el puntero
archivo_texto.seek(0)
print(archivo_texto.read(30))

#con una operacion matematica
archivo_texto.seek(0)
archivo_texto.seek(len(archivo_texto.read())/2)
print(archivo_texto.read())

#para leer una linea especifica
archivo_texto.seek(1)
archivo_texto.seek(len(archivo_texto.readline()))
print(archivo_texto.read())


# para lectura y escritura simultaneamente
archivo_texto=open("archivo.txt", "r+") # lectura y escritura
archivo_texto.seek(len(archivo_texto.read()))
archivo_texto.write("Final del texto")
print(archivo_texto.read())

archivo_texto.close()


