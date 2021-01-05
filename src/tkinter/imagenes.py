from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")
ventana.title("Hola Mundo")
ventana.resizable(0, 0)

# Imagenes

imagen = Image.open("./img/informatica.jpg")
render = ImageTk.PhotoImage(imagen)
Label(ventana, image=render).pack()

ventana.mainloop()