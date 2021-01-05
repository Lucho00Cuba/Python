from tkinter import *

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Hola Mundo")
ventana.resizable(0, 0)

# Textos

texto = Label(ventana, text="Bienvenido")
texto.config(
    justify=RIGHT,
    bg="green",
    width=5,
    height=5,
    cursor="spider"
)
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text="Basico")
texto.config(
    height=3,
    fg="white",
    bg="black",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT)

texto = Label(ventana, text="Intermedio")
texto.config(
    height=3,
    bg="red",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT)

texto = Label(ventana, text="Avanzado")
texto.config(
    height=3,
    bg="orange",
    font=("Arial", 18),
    padx=10,
    pady=20,
    cursor="spider"
)
texto.pack(side=LEFT)

ventana.mainloop()