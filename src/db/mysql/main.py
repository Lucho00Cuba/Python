import mysql.connector

# Conexion
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master"
)

# Validacion de connecion
#print(database)

# Cursor

cursor = database.cursor()

# Creando Base de Datos
cursor.execute("CREATE DATABASE IF NOT EXISTS master")
cursor.execute("SHOW DATABASES")

for i in cursor:
    print(i)

# Creando Tablas

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES")

for t in cursor:
    print(t)

# Insertar registros

#cursor.execute("INSERT INTO vehiculos VALUES (null, 'Opel', 'Astra', 18500)")

coches = [
    ('Seat','Ibiza',5000),
    ('Renault','Clio',15000),
    ('Citroen','Saxo',2000),
    ('Mercedez','Clase C',35000)
]

#cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)

database.commit()

# Leer datos de una tabla

cursor.execute("SELECT *  FROM vehiculos")

result = cursor.fetchall()

for i in result:
    print(i[1])

# Borrar datos

cursor.execute("DELETE FROM vehiculos WHERE marca = 'Citroen' ")
database.commit()

print(cursor.rowcount, "borrados!!")

# Actualizar

cursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca = 'Seat' ")
database.commit()