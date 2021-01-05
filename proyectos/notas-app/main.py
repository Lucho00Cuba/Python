# App Notas


# Importaciones de Modulos
from usuarios import acciones

print("""
    Acciones Disponibles

    - [1] registro
    - [2] login
""")

hazEL = acciones.Acciones()

accion = int(input("Que kieres hacer?: "))

if accion == 1:
    hazEL.registro()
elif accion == 2:
   hazEL.login()
else:
    print("Opcion Invalida")