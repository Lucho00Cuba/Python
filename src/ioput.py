####################
# Entrada & Salida #
#       Datos      #
#   Autor: Lucho   #
####################

nombre = input("Introduce tu nombre: ") # -> Funcion input nos permite que un usuario introduzca datos
edad = int(input("Introduce tu edad: ")) # -> Metodo 1
edad = int(edad) # -> Metodo 2

# Salida
print("Tu nombre es {n}".format(n=nombre))
print("Tu edad es {e}".format(e=edad))