###################
#   Excepciones   #
#                 #
#   Autor: Lucho  #
###################
"""
try:
    nombre = input("Cual es tu nombre: ")

    if len(nombre) >= 1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)
except:
    print("Ha ocurrido un error, introduce bien el nombre")
else:
    print("todo ha funcionado correctamente")
finally:
    print("Fin de la iteracion")
"""

# Multiples excepciones
"""
try:
    num = input("Introduce un numero: ")
    print(f"El cuadrado es: {num*num}")
except Exception as e:
    print("Ha ocurrido un error ", type(e).__name__)
except ValueError:
    print("Introduce un numero, no un texto")
"""

# Excepciones Personalizadas

try:
    nombre = input("Cual es tu nombre: ")
    edad = int(input("Caul es tu edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre) <= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print("Bienvenido")
except ValueError:
    print("Introduce los datos correctamente")
except Exception as e:
    print(e)