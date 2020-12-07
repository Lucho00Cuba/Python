# Funciones

"""
Funciones : Fragmentos de codigos que se pueden ejecutar multiples veces. Pueden recibir y devovler informacion para comunicarse con el proceso principal
"""

def funcion(): # <- Definiendo la funcion
    print("Hola Mundo") # <- Codigo que ejecutara la funcion en su llamada
funcion() # <- Llamando la funcion

# Ejemplo

def dibujar_tabla_del_5():
    for i in range(11):
        print("5 * {numero} = {resultado}".format(numero=i,resultado=i*5))

dibujar_tabla_del_5()

#  Funciones con sus variables

# Variable dentro de la funcion, no existe el proceso principal.
def test():
    n = 10
#print(n) <- Genera un NameError


# Variable fuera de la funcion

m = 10 
def test():
    print(m)
test()

# Dos Variables


def test():
    o = 5 # <- Declaracion de variable
    print(o)
test()
o = 10 # <- Tratando de asignarle otro valor
test()
print(o)

# """ Analizando el codigo anterior se puede ver que se declaran una variable dentro de la funcion, y en el proceso principal se le asigna otro valor.
# Pero lo que realmente sucede es que al declarar la variable dentro de la funcion, cuando tratamos de asginar otro valor a la variable en el proceso 
# principal lo que realmente pasa es que se crea una variable en el proceso principal llamado "o"."""