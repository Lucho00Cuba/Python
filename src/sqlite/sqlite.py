import sqlite3

# Conexion

conexion = sqlite3.connect('pruebas.db')

# Crear cursor

cursor = conexion.cursor()

# Crear tabla

cursor.execute("""CREATE TABLE IF NOT EXISTS productos( 
id INTEGER PRIMARY KEY AUTOINCREMENT,
titulo varchar(255),
description TEXT,
precio int(10)
)""")

# Guardas Cambios

conexion.commit()

"""
# Insertar datos

cursor.execute("INSERT INTO productos VALUES (null, 'Producto 1', 'Descripcion de mi producto', 550)")
conexion.commit()

# Listar datos

cursor.execute("SELECT * FROM productos;")

print(cursor)
productos = cursor.fetchall()

print(productos)

for p in productos:
    print(p)
"""

# Insertar registros

productos = [
    ("Portatil", "Buen Pc", 700),
    ("Apple", "Buen Movil", 1000),
    ("Soni", "Buen Sonido", 200),
]

cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos) 
conexion.commit()

# Borrar registros
#cursor.execute("DELETE FROM productos")
#conexion.commit()

# Actualizar

cursor.execute("UPDATE productos SET precio=678 WHERE precio = 200")
conexion.commit()

# Cerrar la conexion

conexion.close()