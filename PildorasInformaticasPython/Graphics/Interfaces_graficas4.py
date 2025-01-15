# Creacion de interfaces graficas widget Entry
"""
- Widgets utilizados para mostrar texto o imagenes.

- Tienen como unica finalidad mostrar texto, no se puede interactuar con él (borrar, arrastrar, etc)
"""

from tkinter import *

root=Tk()

myFrame=Frame(root, width=1200, height=800)
myFrame.pack()

LabelName=Label(myFrame, text="Name :")
LabelName.grid(row=0, column=0, sticky='e', padx=10, pady=10)

LabelLastName=Label(myFrame, text="Last name :")
LabelLastName.grid(row=1, column=0, sticky='e', padx=10, pady=10)

LabelAddress=Label(myFrame, text="Address :")
LabelAddress.grid(row=2, column=0, sticky='e', padx=10, pady=10)

LabelAddress=Label(myFrame, text="Address :")
LabelAddress.grid(row=2, column=0, sticky='e', padx=10, pady=10)

LabelPassword=Label(myFrame, text="Password :")
LabelPassword.grid(row=3, column=0, sticky='e', padx=10, pady=10)

cuadroName=Entry(myFrame)
cuadroName.grid(row=0, column=1)
cuadroName.config(fg="red", justify="left")

cuadroLastName=Entry(myFrame)
cuadroLastName.grid(row=1, column=1)

cuadroAddress=Entry(myFrame)
cuadroAddress.grid(row=2, column=1)

cuadroPassword=Entry(myFrame)
cuadroPassword.grid(row=3, column=1)
cuadroPassword.config(show="*")


root.mainloop()