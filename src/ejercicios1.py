###################
#  Ejercicios 1   #
#                 #
#   Autor: Lucho  #
###################
"""
print("#### Ejercicio 1 ####")

lista = [1,8,5,6,3,4,7,2] # -> Creando una lista
print(lista)

#for i in lista: # -> Recorriendo lista
#    print(i)

def running(li): # -> Funcion 
    resultado = ""
    for i in li:
        resultado += "Elemento: " + str(i)
        resultado += "\n"

    return resultado

print(running(lista))


lista.sort()
print(lista) # -> Mostrando lista ordenada
print(len(lista)) # -> Mostrando longitud de la lista

num = int(input("Introduce un numero: "))
comprobar = isinstance(num, int)
while not comprobar or num <= 0:
    num = int(input("Introduce un numero: "))
else:
    print(f"Has introduce el {num}")
print(lista.index(num)) # -> Buscando Elemento
"""
"""
print("#### Ejercicio 2 ####")

num = []
### While
x = 0

while x < 120:
    num.append(f"Elemento-{x}")
    print("Mostrando el: " + num[x])
    x += 1 
print(num[77]) 

### For
for contador in range(0, 120):
    num.append(f"Elemento-{contador}")
    print("Mostrando el: " + num[contador])
print(num)
"""
"""
print("#### Ejercicio 3 ####")

texto = ""

if len(texto.strip()) <=0:
    texto = "hola soy un texto en minusculas"
    print(texto.upper())
else:
    print(f"La variable tiene contenido: {texto}")
"""
"""
print("#### Ejercicio 4 ####")

def traducir(tipo):
    result = None
    if tipo == list:
        result = "LISTA"
    elif tipo == str:
        result = "CADENA DE TEXTO"
    elif tipo == int:
        result = "NUMERO ENTERO"
    elif tipo == bool:
        result = "BOOLEANO"
    else:
        result = "ERROR"
    return result


def comprobar(var, tipo):
    test = isinstance(var, tipo)
    result = ""
    if test:
        result = f"Este dato es del tipo {traducir(tipo)}"
    else:
        result = "El tipo de dato no es correcto"
    return result

lista = ["hola mundo",2]
cadena = "Linux"
num = 1
booleano = True

print(comprobar(num, int))
print(comprobar(booleano, bool))
print(comprobar(cadena, str))
print(comprobar(lista, list))
"""
"""
print("#### Ejercicio 5 ####")

tabla = [
    {
        "categoria":"accion",
        "juegos": ["GTA","COD","PUGB"]
    },
    {
        "categoria":"aventuras",
        "juegos": ["ASSASINS","CRASH","PRINCE OF PERSIA"]
    },
    {
        "categoria":"deportes",
        "juegos": ["FIFA", "PES", "MOTO GP"]
    }
]

for c in tabla:
    print(f"----------{c['categoria']}----------")
    for j in c['juegos']:
        print(j)
"""