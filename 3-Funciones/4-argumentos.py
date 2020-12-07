# Funciones

# Argumentos por posicion

def resta(a,b):
    return a-b

l = resta(a=2,b=1)
print(l)

def resta(a=None,b=None):
    if a == None or b == None:
        print("Error, enviar dos valores a la funcion")
    else:
        return a-b
l = resta()
print(l)