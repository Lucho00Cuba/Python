# Errores

# Sintacticos

#print("Hola Mundo" # <- Se esparaba terminar con un ")"
#pint("Hola Mundo") # <- La funcion correcta es print

# Semanticos

l = [1,2,3]
l.pop()
l.pop()
l.pop()
#l.pop() # <- Lista Vacia

n = float(input("Introduce un numero: "))
m = 4
print("{n}/{m}={r}".format(n=n,m=m,r=n/m)) # <- Variable "n" contiene una cadena y no un entero