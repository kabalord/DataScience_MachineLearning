# Creacion de interfaces graficas FRAME

"""
- Configurar el FRAME
"""

from tkinter import *

root=Tk()

root.title("Ventana de pruebas")

# para impedir que se redimensione la ventana
#root.resizable(True,True)

# Incluir el ico
root.iconbitmap("snake1.ico")

# Definir una dimension de la ventana
#root.geometry("800x600")

#cambiar caracteristicas de color
root.config(bg="blue")

myFrame=Frame()

myFrame.pack()

myFrame.config(bg="red")

myFrame.config(width="800", height="600")

myFrame.config(bd=35)

myFrame.config(relief="sunken")

myFrame.config(cursor="pirate")

# Esta linea de codigo debe permanecer siempre en el ultimo lugar
root.mainloop()