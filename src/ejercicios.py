###################
#   Ejercicios    #
#                 #
#   Autor: Lucho  #
###################

# Inicio del Comentario
"""

print("##### Ejercicio 1 #####")

pais = "Cuba" # -> Tipo de dato (cadena de texto)
continente = "America" # -> Tipo de dato (cadena de texto)

print(f"{pais} - {continente} ")
print("{p} - {c}".format(p=pais, c=continente))

##################################################

print("##### Ejercicio 2 #####")

for i in range(1, 101):
    if i % 2 == 0:
        print(f"El numero {i} es par")
    
##################################################

print("##### Ejercicio 3 #####")

for i in range(1, 61):
    print(f"El cuadrado con for de {i} es {i*i}")


contador = 1
while contador <= 60:
    print(f"El cuadrado con while de {contador} es {contador*contador}")

    contador += 1


print("##### Ejercicio 4 #####")
num_one = int(input("Introduce un numero: "))
num_two = int(input("Introduce otro numero: "))

print(f"Numero 1: {num_one} ; Numero 2: {num_two}")
print(f"Suma : {num_one+num_two}")
print(f"Resta : {num_one-num_two}")
print(f"Multiplicacion : {num_one*num_two}")
print(f"Division : {num_one/num_two}")
print(f"Resto : {num_one%num_two}")



print("##### Ejercicio 5 #####")
num_one = int(input("Introduce un numero: "))
num_two = int(input("Introduce otro numero: "))

if num_one < num_two:
    num_two += 1
    for i in range(num_one, num_two):
        print(i)
else:
    print("El primer numero debe ser menor al segundo numero")



print("##### Ejercicio 6 #####")

contador = 1

while contador <= 10:
    print("#######################")
    print(f"##### Tabla del {contador} #####")
    print("#######################")

    for i in range(1, 11):
        print(f"{contador} x {i} = {i*contador}")
        
    print("\n")
    contador += 1

 

print("##### Ejercicio 7 #####")
num_one = int(input("Introduce un numero: "))
num_two = int(input("Introduce otro numero: "))

if num_one < num_two:
    for i in range(num_one, (num_two + 1)):
        if i % 2 == 0:
            print(f"{i} es PAR")
        else:
            print(f"{i} es IMPAR")
else:
    print("Numero 1 tiene que ser mayor al Numero 2")

  

print("##### Ejercicio 8 #####")
num_one = int(input("Introduce un numero: "))
porcent = int(input("Que porcentaje: "))

if num_one >= 1 and porcent >= 1:
    operacion = num_one * (porcent/100)
    operacion = int(operacion)
    print(f" El {porcent}% de {num_one} es {operacion}")



print("##### Ejercicio 9 #####")

contador = 1
while True and contador < 100:
    num  = int(input("Introduce un numero: "))
    if num != 111:
        print(num)
        contador += 1
        continue
    else:
        print("numero correcto, Adios!!!")
        break



print("##### Ejercicio 10 #####")

contador = 1
aprobados = 0
suspendidos = 0
num_alumnos = int(input("Cuanto Alumnos tienes?: "))

while contador <= num_alumnos:
    nota = int(input(f"Escriba la nota para alumno {contador}: "))
    contador += 1
    if nota >= 5:
        aprobados += 1
    else:
        suspendidos += 1

print(f"Ahi {aprobados} alumnos aprobados")
print(f"Ahi {suspendidos} alumnos suspendidos")

""" 
# Fin del Comentario