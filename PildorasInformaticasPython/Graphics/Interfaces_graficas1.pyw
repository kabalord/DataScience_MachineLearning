# Creacion de interfaces graficas RAIZ

"""
- Libreria Tkinter : es un puente entre python y la libreria TCL/TK

- Tambien denominadas GUI, son intermediarios entre el programa y el usuario.
Formadas por un conjunto de graficos como ventanas, botones, menus casillas de verificacion etc.

instalacion :
sudo apt-get install python3-tk

-widgets o componentes

- Para cambiar el icono incluir la imagen con extension .ico
utilizar un convertidor .ico
"""
# Init Interface
from tkinter import *

root=Tk()

root.title("Ventana de pruebas")

# para impedir que se redimensione la ventana
root.resizable(True,True)

# Incluir el ico
root.iconbitmap("snake1.ico")

# Definir una dimension de la ventana
root.geometry("800x600")

#cambiar caracteristicas de color
root.config(bg="blue")

# Esta linea de codigo debe permanecer siempre en el ultimo lugar
root.mainloop()
