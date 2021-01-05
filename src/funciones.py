###################
#    Funciones    #
#                 #
#   Autor: Lucho  #
###################

"""
#### Ejemplo 1 ####
def suma(a, b):
    return a+b

resultado = suma(1,1)
print(resultado)
"""
"""
#### Ejemplo 2 ####
def mostrarNombre(name):
    print(f"Tu nombre es {name}")

nombre = input("Introduce tu Nombre: ")
mostrarNombre(nombre)
"""
"""
### Ejemplo 3 ####
def tabla(num):
    print(f"Tabla de Multiplicar del {num}")
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")

    print("\n")

tabla(1)
tabla(4)
"""
"""
### Ejemplo 4 ####
def getEmpleado(name, dni=None):
    print("EMPLEADO")
    print(f"Nombre: {name}")
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Lucho", 123)
getEmpleado("Linux")
"""

"""
### Ejemplo 5 ####
def calc(num_one, num_two, basicas=False):
    
    suma = num_one + num_two
    resta = num_one - num_two
    multi = num_one * num_two
    divi = num_one / num_two
    operacion = ""
    if basicas != False:   
        operacion += "Suma: " + str(suma)
        operacion += "\n"
        operacion += "Resta: " + str(resta)
    else:
        operacion += "\n"
        operacion += "Multi: " + str(multi)
        operacion += "\n"
        operacion += "Division: " + str(divi)
    return operacion

resul = calc(5,5,True)
print(resul)
"""

"""
### Ejemplo 6 ####
def getNombre(name):
    texto = f"El nombre es: {name}"
    return texto

def getNick(nick):
    texto = f"El nick es: {nick}"
    return texto

def devuelveTodo(name, nick):
    texto = getNombre(name) + "\n" + getNick(nick)
    return texto

print(getNombre("Lucho"), getNick("Linux"))
print(devuelveTodo("Lucho","Linux"))
"""

"""
### Ejemplo 7 ####

year = lambda year: f"El año es {year}"

print(year(2032))
"""