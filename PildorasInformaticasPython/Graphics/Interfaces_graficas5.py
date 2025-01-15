# Creacion de interfaces graficas widgets Text y Button

"""
- Text: Widgets utilizados para introducir texto largo.

- Button: Botones para interactuar con la interfaz

- Scrollbar para descender con el ascensor
"""

from tkinter import *

root=Tk()

myFrame=Frame(root, width=1200, height=800)
myFrame.pack()

myName=StringVar()

LabelName=Label(myFrame, text="Name :")
LabelName.grid(row=0, column=0, sticky='e', padx=10, pady=10)

LabelLastName=Label(myFrame, text="Last name :")
LabelLastName.grid(row=1, column=0, sticky='e', padx=10, pady=10)

LabelAddress=Label(myFrame, text="Address :")
LabelAddress.grid(row=2, column=0, sticky='e', padx=10, pady=10)

LabelPassword=Label(myFrame, text="Password :")
LabelPassword.grid(row=3, column=0, sticky='e', padx=10, pady=10)

#Interfaces_graficas 5
LabelComments=Label(myFrame, text="Comentarios :")
LabelComments.grid(row=4, column=0, sticky='e', padx=10, pady=10)

cuadroName=Entry(myFrame, textvariable=myName)
cuadroName.grid(row=0, column=1)
cuadroName.config(fg="red", justify="left")

cuadroLastName=Entry(myFrame)
cuadroLastName.grid(row=1, column=1)

cuadroAddress=Entry(myFrame)
cuadroAddress.grid(row=2, column=1)

cuadroPassword=Entry(myFrame)
cuadroPassword.grid(row=3, column=1)
cuadroPassword.config(show="*")

#Interfaces_graficas5
cuadroComments=Text(myFrame, width=16, height=5)
cuadroComments.grid(row=4, column=1, padx=20, pady=20)

#scroll
scrollVert=Scrollbar(myFrame, command=cuadroComments.yview)
cuadroComments.config(yscrollcommand=scrollVert.set)
scrollVert.grid(row=4, column=2, pady=10, sticky='nse')

#button

def buttonCode():
    myName.set("Walter")


buttonSend=Button(root, text="Enviar", command=buttonCode)
buttonSend.pack()

root.mainloop()