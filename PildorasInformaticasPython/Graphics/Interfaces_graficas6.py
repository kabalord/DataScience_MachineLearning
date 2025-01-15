# Creacion de interfaces graficas CALCULADORA INTERFACE

from tkinter import *

root=Tk()

mi_frame=Frame(root)
mi_frame.pack()

#----------------PANTALLA-----------------#
pantalla=Entry(mi_frame)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="#000000", fg="#03f943", justify="right")



#----------------FILA 1-----------------#
boton7=Button(mi_frame, text="7", width=3)
boton7.grid(row=2, column=1)

boton8=Button(mi_frame, text="8", width=3)
boton8.grid(row=2, column=2)

boton9=Button(mi_frame, text="9", width=3)
boton9.grid(row=2, column=3)

botonDiv=Button(mi_frame, text="/", width=3)
botonDiv.grid(row=2, column=4)


#----------------FILA 2-----------------#
boton4=Button(mi_frame, text="4", width=3)
boton4.grid(row=3, column=1)

boton5=Button(mi_frame, text="5", width=3)
boton5.grid(row=3, column=2)

boton6=Button(mi_frame, text="6", width=3)
boton6.grid(row=3, column=3)

botonMult=Button(mi_frame, text="*", width=3)
botonMult.grid(row=3, column=4)


#----------------FILA 3-----------------#
boton1=Button(mi_frame, text="1", width=3)
boton1.grid(row=4, column=1)

boton2=Button(mi_frame, text="2", width=3)
boton2.grid(row=4, column=2)

boton3=Button(mi_frame, text="3", width=3)
boton3.grid(row=4, column=3)

botonRest=Button(mi_frame, text="-", width=3)
botonRest.grid(row=4, column=4)


#----------------FILA 4-----------------#
boton0=Button(mi_frame, text="0", width=3)
boton0.grid(row=5, column=1)

botonColon=Button(mi_frame, text=",", width=3)
botonColon.grid(row=5, column=2)

botonEgal=Button(mi_frame, text="=", width=3)
botonEgal.grid(row=5, column=3)

botonPlus=Button(mi_frame, text="+", width=3)
botonPlus.grid(row=5, column=4)




root.mainloop()