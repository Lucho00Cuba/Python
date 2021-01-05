# Calculadora
#
# By
#
# Lucho
"""
from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")
ventana.config(
    bd=25
)

# Funciones

def cFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror("Error", "Introduce bien los datos")

    return result

def sumar():
    result.set(cFloat(num_1.get()) + cFloat(num_2.get()))
    mostrarResult()

def restar():
    result.set(cFloat(num_1.get()) - cFloat(num_2.get()))
    mostrarResult()

def multiplicar():
    result.set(cFloat(num_1.get()) * cFloat(num_2.get()))
    mostrarResult()

def dividir():
    result.set(cFloat(num_1.get()) / cFloat(num_2.get()))
    mostrarResult()

def mostrarResult():
    messagebox.showinfo("Resultado", f"El resultado es {result.get()}")
    num_1.set("")
    num_2.set("")

marco = Frame(ventana, width=250, height=250)
marco.config(
    bd=5,
    relief=SOLID,
    padx=15,
    pady=15
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

num_1 = StringVar()
num_2 = StringVar()
result = StringVar()

Label(marco, text="Primer numero").pack()
Entry(marco, textvariable=num_1, justify=CENTER).pack()

Label(marco, text="Segundo numero").pack()
Entry(marco, textvariable=num_2, justify=CENTER).pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Dividir", command=dividir).pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()
"""

## Refactorizando Codigo

# Calculadora
#
# By
#
# Lucho

from tkinter import *
from tkinter import messagebox

class Calculadora:

    # Funciones
    def __init__(self, alertas):
        self.num_1 = StringVar()
        self.num_2 = StringVar()
        self.result = StringVar()
        self.alertas = alertas



    def cFloat(self, numero):
        try:
            result = float(numero)
        except:
            result = 0
            messagebox.showerror("Error", "Introduce bien los datos")

        return result

    def sumar(self):
        self.result.set(self.cFloat(self.num_1.get()) + self.cFloat(self.num_2.get()))
        self.mostrarResult()

    def restar(self):
        self.result.set(self.cFloat(self.num_1.get()) - self.cFloat(self.num_2.get()))
        self.mostrarResult()

    def multiplicar(self):
        self.result.set(self.cFloat(self.num_1.get()) * self.cFloat(self.num_2.get()))
        self.mostrarResult()

    def dividir(self):
        self.result.set(self.cFloat(self.num_1.get()) / self.cFloat(self.num_2.get()))
        self.mostrarResult()

    def mostrarResult(self):
        self.alertas.showinfo("Resultado", f"El resultado es {self.result.get()}")
        self.num_1.set("")
        self.num_2.set("")

ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")
ventana.config(
    bd=25
)

calculadora = Calculadora(messagebox)

marco = Frame(ventana, width=250, height=250)
marco.config(
    bd=5,
    relief=SOLID,
    padx=15,
    pady=15
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer numero").pack()
Entry(marco, textvariable=calculadora.num_1, justify=CENTER).pack()

Label(marco, text="Segundo numero").pack()
Entry(marco, textvariable=calculadora.num_2, justify=CENTER).pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=calculadora.sumar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Restar", command=calculadora.restar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Multiplicar", command=calculadora.multiplicar).pack(side=LEFT, fill=X, expand=YES)
Button(marco, text="Dividir", command=calculadora.dividir).pack(side=LEFT, fill=X, expand=YES)

ventana.mainloop()