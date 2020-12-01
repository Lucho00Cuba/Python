# Sentencias de Control

"""
Condicionales : Para elegir entre distintas posibilidades

Iterativas : Para repetir un bloque de intrucciones
"""

# Condicionales

## Sentencia IF (Si)
#
#a = 5
#b = 10
#
#if a == 2:
#    print("a vale 2")
#if a == 5:
#    print("a vale 5")
#
#if a == 5 and b == 10:
#    print("a vale 5 y b vale 10")
#
#n = 10
#if n % 2 == 0:
#    print(n,"es un numero par")
#else:
#    print(n,"es un numero impar")
#
## Setencia ELIF (Sino si)
#
#comand = "Salir"
#
#if comand == "Entrar":
#    print("Bienvenido al sistema")
#elif comand == "Saludar":
#    print("Hola Mundo")
#elif comand == "Salir":
#    print("Saliendo del sistema")
#else:
#    print("No se reconoce el comando")
#
## Iterativas
#
## Sentencia While (Mientras)
#
#var = 0
#while var < 5:
#    var += 1
#    if (var == 4):
#        print("Se rompe el bucle cuando vale",var)
#        break # Romper el bluce
#        continue # Saltar la iteracion
#    print("Var vale",var)
#else:
#    print("Var ya vale",var)
#
## Ejemplo
#
#print("Bienvenido al Menu")
#
#while (True):
#    print("""Que quieres hacer 
#    1) Saludar
#    2) Sumar dos numeros
#    3) Salir""")
#    opcion = input()
#    if opcion == '1':
#        print("Hola, como estas ! ")
#    elif opcion == '2':
#        n1 = float(input("Primer Numero : "))
#        n2 = float(input("Segundo Numero : "))
#        print("El resultado es: ",n1+n2)
#    elif opcion == '3':
#        print("Adios")
#        break
#    else:
#        print("Comando desconocido")
#
## Sentencia FOR

numeros = [1,2,3,4,5,6,7,8,9,10]
#indice = 0

# Iterar en una lista con While
#while(indice < len(numeros)):
#    print(numeros[indice])
#    indice+=1
#
# Iterar en una lista con FOR
#for numero in numeros:
#    print(numero)

# Editar valores de una lista al vuelo 
#for numero in numeros:
#    numeros[indice] *= 10
#    indice += 1
#print(numeros)

# Editar al vuelo con enumerate
#for indice,numero in enumerate(numeros):
#    numeros[indice] *= 10
#print(numeros)

cadena = "Hola Mundo"
cadena2 = ""

for caracter in cadena:
    cadena2 += "*"
    print(caracter)
print(cadena2)

for i in range(10):
    print(i)

print(list(range(10)))