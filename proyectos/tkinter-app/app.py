
from tkinter import *
from tkinter import ttk

# Definir Ventana
ventana = Tk()
ventana.title("Proyecto")
#ventana.geometry("500x500")
ventana.minsize(500, 500)
ventana.resizable(0, 0)

# Pantallas
def home():
    # Mostrar Pantalla
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=210,
        pady=20
    )
    home_label.grid(row=0, column=0)

    products_box.grid(row=2)

    # Listar Productos
    """
    for p in products:
        if len(p) == 3:
            p.append("Added")
            Label(products_box, text=p[0]).grid()
            Label(products_box, text=p[1]).grid()
            Label(products_box, text=p[2]).grid()
            Label(products_box, text="-----------------").grid()
    """
    for p in products:
        if len(p) == 3:
            p.append("Added")
            products_box.insert('', 0, text=p[0], values=(p[1]))

    # Ocultar Pantallas

    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove()

    return True


def add():
    # Mostrar Pantalla
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=110,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=10)

    # Campos del Formulario
    add_frame.grid(row=1)

    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=E)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=E)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )

    # Separador
    add_separator.grid(row=4)

    # Boton
    boton.grid(row=5, column=1, sticky=NW)
    boton.config(
        fg="white",
        bg="green",
        padx=15,
        pady=5
    )

    # Ocultar Pantallas

    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    products_box.grid_remove()

    return True

def info():
    # Mostrar Pantalla
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=150,
        pady=20
    )
    info_label.grid(row=0, column=0)

    data_label.grid(row=1, column=0)

    # Ocultar Pantallas
    home_label.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()
    products_box.grid_remove()

    return True

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0","end-1c")
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", "end-1c")

    home()

# Variables
name_data = StringVar()
price_data = StringVar()
products = []

# Definir campos de pantallas

# Inicio
home_label = Label(ventana, text="Inico")
#products_box = Frame(ventana, width=250)

Label(ventana).grid(row=1)

products_box = ttk.Treeview(height=12,columns=2)
products_box.grid(row=1, column=0, columnspan=2)
products_box.heading("#0", text="Producto", anchor=W)
products_box.heading("#1", text="Precio", anchor=W)

# Añadir
add_label = Label(ventana, text="Añadir Producto")

# Campos del Formulario
add_frame = Frame(ventana)

# Data
add_name_label = Label(add_frame, text="Nombre: ")
add_name_entry = Entry(add_frame,textvariable=name_data)

# Price
add_price_label = Label(add_frame, text="Precio: ")
add_price_entry = Entry(add_frame,textvariable=price_data)

add_description_label = Label(add_frame, text="Descripcion: ")
add_description_entry = Text(add_frame)

# Separador
add_separator = Label(add_frame, text="")

# Button
boton = Button(add_frame, text="Guardar", command=add_product)

# Informacion
info_label = Label(ventana, text="Informacion")
data_label = Label(ventana, text="Creado por Lucho")

# Cargar pantalla de inicio
home()

# ---------------------------------------------- #

# Menu Superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Informacion", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

# Cargar Menu
ventana.config(menu=menu_superior)

# Cargar Ventana
ventana.mainloop()