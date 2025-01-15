# Creacion de interfaces graficas CALCULADORA FUNCTIONALITY

from tkinter import *

root=Tk()

mi_frame=Frame(root)
mi_frame.pack()

#----------------PANTALLA-----------------#

#definicion de variables

numeroPantalla=StringVar()




pantalla=Entry(mi_frame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="#000000", fg="#03f943", justify="right")

#---------------Pulsaciones teclado-------------------------#
def numero_pulsado(num):
    numeroPantalla.set(numeroPantalla.get() + num)

#----------------FILA 1-----------------#
boton7=Button(mi_frame, text="7", width=3, command=lambda:numero_pulsado("7"))
boton7.grid(row=2, column=1)

boton8=Button(mi_frame, text="8", width=3, command=lambda:numero_pulsado("8"))
boton8.grid(row=2, column=2)

boton9=Button(mi_frame, text="9", width=3, command=lambda:numero_pulsado("9"))
boton9.grid(row=2, column=3)

botonDiv=Button(mi_frame, text="/", width=3)
botonDiv.grid(row=2, column=4)


#----------------FILA 2-----------------#
boton4=Button(mi_frame, text="4", width=3, command=lambda:numero_pulsado("4"))
boton4.grid(row=3, column=1)

boton5=Button(mi_frame, text="5", width=3, command=lambda:numero_pulsado("5"))
boton5.grid(row=3, column=2)

boton6=Button(mi_frame, text="6", width=3, command=lambda:numero_pulsado("6"))
boton6.grid(row=3, column=3)

botonMult=Button(mi_frame, text="*", width=3)
botonMult.grid(row=3, column=4)


#----------------FILA 3-----------------#
boton1=Button(mi_frame, text="1", width=3, command=lambda:numero_pulsado("1"))
boton1.grid(row=4, column=1)

boton2=Button(mi_frame, text="2", width=3, command=lambda:numero_pulsado("2"))
boton2.grid(row=4, column=2)

boton3=Button(mi_frame, text="3", width=3, command=lambda:numero_pulsado("3"))
boton3.grid(row=4, column=3)

botonRest=Button(mi_frame, text="-", width=3)
botonRest.grid(row=4, column=4)


#----------------FILA 4-----------------#
boton0=Button(mi_frame, text="0", width=3, command=lambda:numero_pulsado("0"))
boton0.grid(row=5, column=1)

botonColon=Button(mi_frame, text=",", width=3, command=lambda:numero_pulsado(","))
botonColon.grid(row=5, column=2)

botonEgal=Button(mi_frame, text="=", width=3)
botonEgal.grid(row=5, column=3)

botonPlus=Button(mi_frame, text="+", width=3)
botonPlus.grid(row=5, column=4)




root.mainloop()