from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Hola Mundo")
#ventana.resizable(0, 0)
ventana.config(
    bd=50
)

def sacarAlerta():
    MessageBox.showerror("Alerta", "Lucho")

Button(ventana, text="Mostrar alerta", command=sacarAlerta).pack()

def salir(nombre):
    result = MessageBox.askquestion("Salir", "Quieres salir")

    if result != "yes":
        MessageBox.showinfo("Chao", f"Adios {nombre}")
        ventana.destroy()

Button(ventana, text="Salir", command=lambda: salir("Lucho")).pack()

ventana.mainloop()