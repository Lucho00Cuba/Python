# Tkinter
#
# Modulo para crear intrerfaces graficas de usuario
#

from tkinter import *
import os.path

class Programa:

    def __init__(self):

        self.title = "Python Ventana"
        self.icon = "./img/favicon.ico"
        self.size = "770x470"
        self.resizable = False

    def cargar(self):

        # Crear Ventana Raiz
        ventana = Tk()
        self.ventana = ventana

        # Titulo de la ventana
        ventana.title(self.title)

        # Ruta icono
        ruta_icono = os.path.abspath(self.icon)

        # Icono
        ventana.iconbitmap(ruta_icono)

        # Mostrar texto en el programa

        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # Cambio en el Tamaño
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)


    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()
        # Arranar y Mostrar la ventana hasta que se cierre
        # ventana.mainloop()

# Instanciar mi programa

programa = Programa()
programa.cargar()
programa.addTexto("Hola")
programa.mostrar()