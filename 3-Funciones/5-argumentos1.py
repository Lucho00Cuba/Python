# Funciones

# Argumentos por valor

# Valor no se modifica en la variable nativa
def doblar_valor(numero):
    numero*=2
    print(numero)
n = 10
doblar_valor(n)
print(n)

# Valor si se modifica en la variable nativa
def doblar_valor(numero):
    return numero * 2
n = 10
n = doblar_valor(n)
print(n)

# Valor no se modifica en la lista de la variable nativa
def doblar_valor(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [10,50,100]
doblar_valor(ns[:])
print(ns)

# Valor si se modifica en la lista de la variable nativa
def doblar_valor(numeros):
    for i,n in enumerate(numeros):
        numeros[i] *= 2
ns = [10,50,100]
doblar_valor(ns)
print(ns)

# Indeterminados argumentos

def indeterminados_posicion(*args):
    for arg in args:
        print(arg)
indeterminados_posicion(5,"Hola",[1,2,3,4,5])

def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg,"=",kwargs[kwarg])
indeterminados_nombre(n=5,c="Hello",l=[1,2,3,4,5])

# Ambas

def super_funcion(*args,**kwargs):
    t = 0
    for arg in args:
        t+=arg
        print("Sumatoria es",t)
    for kwarg in kwargs:
        print(kwarg,"=",kwargs[kwarg])

super_funcion(10,50,-1,1.56,nombre="Lucho",edad=18)