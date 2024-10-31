# MODULOS

"""
- Atento a las rutas
- Lo primero es importar el modulo
- utilizar la nomenclatura del punto
"""

import maths_function

maths_function.sumar(7,5)

maths_function.restar(7,5)


# Si no quiero poner el nombre puedo llamar la funcion que necesito

from maths_function import sumar

sumar(7,8)


# Si quiero utilizar las funciones sin restriccion sin poner el prefix pongo *
# Tener cuidado con el asterisco porque hay que tener en cuenta la optimizacion y no reservar demasiada memoria

from maths_function import *

sumar(8,9)

restar(2,5)

multiplicar(2,18)
