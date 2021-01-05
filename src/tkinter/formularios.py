"""
from tkinter import *

ventana = Tk()
ventana.geometry("700x400")
ventana.title("Hola Mundo")
#ventana.resizable(0, 0)

# Texto encabezado
encabezado = Label(ventana, text="Formularios con Python Tkinter - Lucho")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=14, sticky=W)

# Label para el campo (nombre)
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

# Campo de Texto (nombre)
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W ,padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

# Label para el campo (apellidos)
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

# Campo de Texto (apellidos)
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W ,padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

# Label para el campo (Descripcion)
label = Label(ventana, text="Descripcion")
label.grid(row=3, column=0, padx=5, pady=5, sticky=N)

# Campo de texto
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(
    width=30,
    height=5,
    font=("Arial", 12),
    padx=15,
    pady=15
)

# Boton
Label(ventana).grid(row=4, column=1)

boton = Button(ventana, text="Enviar")
boton.grid(row=5, column=1, sticky=W)
boton.config(
    padx=10,
    pady=10,
    bg="white",
    fg="black"
)


ventana.mainloop()
"""

from tkinter import *

ventana = Tk()
ventana.geometry("800x500")
ventana.title("Formularios")

encabezado = Label(ventana, text="Formularios 2")
encabezado.config(
    fg="white",
    bg="green",
    padx=15,
    pady=15,
    font=("Consolas", 20)
)
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)

def mostrarProfesion():
    texto = ""
    if dev.get():
        texto += "Desarrollo"

    if sys.get():
        if dev.get():
            texto += " y Sysadmin"
        else:
            texto += "Sysadmin"


    mostrar.config(
        text=texto,
        bg="green",
        fg="White"
    )

dev = IntVar()
sys = IntVar()

# Botones check
Label(ventana, text="A que te dedicas?").grid(row=1, column=0)
Checkbutton(
    ventana,
    text="Desarrollo",
    variable=dev,
    onvalue=1,
    offvalue=0,
    command=mostrarProfesion
).grid(row=2, column=0)

Checkbutton(
    ventana,
    text="Sysadmin",
    variable=sys,
    onvalue=1,
    offvalue=0
).grid(row=3, column=0)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0)

# Radio buttons

def marcar():
    marcado.config(text=opcion.get())


opcion = StringVar()
opcion.set(None)

Label(ventana, text="Genero").grid(row=5)
Radiobutton(
    ventana,
    text="Masculino",
    value="Masculino",
    variable=opcion,
    command=marcar
).grid(row=6, column=0)
Radiobutton(
    ventana,
    text="Feminino",
    value="Femenino",
    variable=opcion,
    command=marcar
).grid(row=7, column=0)

marcado = Label(ventana)
marcado.grid(row=8)

# Option Menu
def seleccionar():
    seleccionado.config(text=opcion.get())


opcion = StringVar()
opcion.set("Opcion 1")

Label(ventana, text="Seleccione una opcion").grid(row=5, column=1)

select = OptionMenu(ventana, opcion, "Opcion 1", "Opcion 2", "Opcion 3")
select.grid(row=6, column=1)

Button(ventana, text="Ver", command=seleccionar).grid(row=7,column=1)

seleccionado = Label(ventana)
seleccionado.grid(row=8, column=1)

ventana.mainloop()