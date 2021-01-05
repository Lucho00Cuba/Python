from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Hola Mundo")
#ventana.resizable(0, 0)
ventana.config(
    bd=50
)
def getdato():
    resultado.set(dato.get())

dato = StringVar()
resultado = StringVar()

Label(ventana, text="Hola Mundo").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)

Label(ventana, text="Dato recogido").pack(anchor=NW)
Label(ventana, textvariable=resultado).pack(anchor=NW)

Button(ventana, text="Mostrar dato", command=getdato).pack(anchor=NW)

ventana.mainloop()