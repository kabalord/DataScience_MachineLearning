# SERIALIZACION

"""
- Serializacion de colecciones.

-Que es ?
 - Consiste en guardar en un fichero externo, una coleccion, un diccionario o incluso un objeto.
 La particularidad es que ese fichero externo sera guardado en un formato de codigo binario.

    - Por ejemplo : si se quiere distribuir un objeto construido en python por a travez de internet,
    el archivo en formato binario facilita la la distribucion o si se quiere almacenar en un dispositivo
    de almacenamiento externo o cuando se quiere almacenar en una base de datos.

    - Para serializar python utiliza una biblioteca llamada PICKLE
        - Método dump(): volcado de datos al fichero binario externo
        - Método load(): carga de los datos del fichero binario externo

    """

import pickle

#creacion de una lista (informacion a volcar)
lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]

#creacion de un fichero externo y permisos de escritura binaria (fichero donde quiero volcar)
fichero_binario=open("lista_nombres", "wb")

#hacer el volcado de la lista en el fichero externo (fichero_binario)
pickle.dump(lista_nombres, fichero_binario)

#cerrar el fichero de la memoria
fichero_binario.close()

#borrar el fichero de la memoria (optional)
del (fichero_binario)


#rescatar y leer la informacion del fichero externo
fichero=open("lista_nombres", "rb")

lista=pickle.load(fichero)

print(lista)
