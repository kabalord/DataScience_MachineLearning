# Creacion de interfaces graficas widget Label

"""
- Widgets utilizados para mostrar texto o images.

- Tienen como unica finalidad mostrar texto, no se puede interactuar con él (borrar, arrastrar, etc)

- Label: Sintaxis

variableLabel = Label(contenedor, opciones)
"""

from tkinter import *

root=Tk()

myFrame=Frame(root, width=500, height=400)

myFrame.pack()



myImage=PhotoImage(file="snake.png")

#myLabel=Label(myFrame, text="Hola mundo")
#abreviado
#Label(myFrame, text="Hola mundo", fg="red", font=("Verdana",18)).place(x=100, y=200)
Label(myFrame, image=myImage).place(x=0, y=0)


root.mainloop()

