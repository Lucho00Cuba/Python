from tkinter import *

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Hola Mundo")
ventana.resizable(0, 0)

# Textos

texto = Label(ventana, text="Bienvenido")
texto.config(
    justify=RIGHT,
    bg="orange",
    width=15,
    height=3,
    cursor="spider"
)
texto.pack(anchor=NW)

texto = Label(ventana, text="Lucho")
texto.config(
    fg="white",
    bg="black",
    padx=500,
    pady=20,
    font=("Arial", 30)
)
texto.pack(anchor=CENTER)

ventana.mainloop()