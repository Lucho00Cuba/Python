###################
#  Condicionales  #
#                 #
#   Autor: Lucho  #
###################

# Condicional IF

print("############## EJEMPLO 1 ##################")

#color = "rojo"
color = "negro" # -> Descomentar este para comprobar la sentencia IF y comentar la anterior linea

if color == "rojo": # -> Si esto se cumple, pues se ejecutare el bloque de instrucciones
    print("El color es {c}".format(c=color))
    print("Enhorabuena")
else: # -> si no se cumple pues se ejecutara este bloque de instrucciones
    print("El color no es {c}".format(c=color))

print("############## EJEMPLO 2 ##################")

#year = input("En que año estamos: ") # -> Entrada de un dato
#year = int(year) # -> Convirtiendo el dato a entero 
year = 2020

if year >= 2021:
    print("Estamos en 2021 en adelante !")
else:
    print("Es un año menor a 2021")

##############################################
# SENTENCIAS IF ANIDADAS

print("############## EJEMPLO 3 ##################")

nombre = "Lucho"
ciudad = "Barcelona"
continente = "Europa"
edad = 99
mayor_edad = 18

if edad >= mayor_edad:
    print("{n} es mayor de edad".format(n=nombre))
    if continente != "Europa":
        print("No estas en Europa")
    else:
        print("Estas en Europa y la ciudad de {c}".format(c=ciudad))
else:
    print("{n} no es mayor de edad".format(n=nombre))

##############################################################
#
# SENTENCIAS ELIF

print("############## EJEMPLO 4 ##################")

dia = 1

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
elif dia == 6:
    print("Es Sabado !!")
elif dia == 7:
    print("Es Domingo :(")
else:
    print("La Semana solo tiene 7 dias")

#################################################
#
# Operadores Logicos con las sentencias de control

print("############## EJEMPLO 5 ##################")

edad_maxima = 65
edad_minima = 18
edad_oficial = 17

if edad_oficial >= edad_minima and edad_oficial <= edad_maxima:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")