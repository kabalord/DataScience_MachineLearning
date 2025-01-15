# Creacion de interfaces graficas RADIOBUTTONS

from tkinter import *

root=Tk()

varOption=IntVar()

def imprimir():
    #print(varOption.get())
    if varOption.get()==1:
        etiqueta.config(text="has elegido masculino")
    else:
        etiqueta.config(text="has elegido femenino")

Label(root, text="Género :").pack()

Radiobutton(root, text="Masculino", variable=varOption, value=1, command=imprimir).pack()

Radiobutton(root, text="Femenino", variable=varOption, value=2, command=imprimir).pack()

etiqueta=Label(root)
etiqueta.pack()



root.mainloop()