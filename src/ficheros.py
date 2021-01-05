###################
#    Ficheros     #
#                 #
#   Autor: Lucho  #
###################

from io import open
import pathlib
import shutil

"""
# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
print(ruta)
archivo = open(ruta, "a+")

# Escribir
archivo.write("********SOY UN TEXTO DESDE PYTHON************\n")

# Cerrar archivo
archivo.close()
"""
"""
# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

# Leer contenido y guardarlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for i in lista:
    print(i)
"""
"""
# Copiar
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/copia.txt"
shutil.copyfile(ruta, ruta_nueva)
"""
"""
# Mover
ruta = str(pathlib.Path().absolute()) + "/copia.txt"
rn = str(pathlib.Path().absolute()) + "/copia1.txt"

shutil.move(ruta, rn)
"""
"""
# Eliminar
import os

ruta = str(pathlib.Path().absolute()) + "/copia1.txt"
#os.remove(ruta)

# Comprobar si un archivo existe

import os.path

print(os.path.abspath("./"))

ruta = os.path.abspath("./" + "fichero_texto.txt")
print(ruta)
if os.path.isfile(ruta):
    print("Existe!!")
else:
    print("No existe")
"""

# Directorios

import os

"""
# Crear carpeta

if not os.path.isdir("./micarpeta"):
    os.mkdir("./micarpeta")
    print("Creado")
else:
    print("Ya existe")

# Eliminar
#os.rmdir("./micarpeta")

# Renombrar & Copiar
import shutil

ruta = "./micarpeta"
rn = "./carpeta copiada"

shutil.copytree(ruta, rn)
"""

ls = os.listdir("./")

for i in ls:
    print(i)