# ARCHIVOS EXTERNOS

"""
- Objetivo : Persistencia de datos
    - Es decir la posibilidad de guardar los datos para que no se pierdan
- Dos alternativas :
    - Manejo de archivos externos
        - binarios
        - texto plano

    - Fases : trabajar con el modulo io python native
        - creacion
        - apertura
        - manipulacion
        - cierre

    - Trabajo con BBDD
"""

from io import open
"""
open(nombre_archivo_abrir, modo)
- modos
    - lectura
    - escritura
    - append (agregar info)
"""

archivo_texto=open("archivo.txt", "w")

#crear archivo con contenido
frase=("Estupendo dia para estudiar Python \n"
       "el jueves")

archivo_texto.write(frase)

#cerrar el archivo en la memoria
archivo_texto.close()


#leer contenido completo

archivo_texto_leer=open("setup.py", "r")

texto=archivo_texto_leer.read()

archivo_texto_leer.close()

print(texto)


#leer contenido linea por linea

archivo_texto_leer_lineas=open("setup.py", "r")

lineas_texto=archivo_texto_leer_lineas.readlines()

archivo_texto_leer_lineas.close()

print(lineas_texto)

#se puede acceder a los elementos de la lista a traves del index
print(lineas_texto[0])

#agregar contenido

archivo_texto_append=open("archivo.txt", "a")

archivo_texto_append.write("\nsiempre es una buena ocasion para ver nuevamente las bases de python")

archivo_texto_append.close()

archivo_texto_leer_append=open("archivo.txt", "r")

texto_append=archivo_texto_leer_append.read()

archivo_texto_leer_append.close()

print(texto_append)
