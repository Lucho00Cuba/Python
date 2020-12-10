# Metodos en Cadenas de Texto

print("Hola Mundo".upper()) # Devuelve todos los caracteres de la cadena en Mayusculas
print("HOLA MUNDO".lower()) #Devuleve todos los caracteres de la cadena en Minusculas
print("hola mundo".capitalize()) # Devuelve la primera letra en Mayuscula
print("hola mundo".title()) # Devuelve las primeras letras en Mayusculas
print("Hola mundo".count('o')) # Devuelve el conteo de la letra "o"
print("Hola Mundo".find('mundo')) # Devuelve el indice de la cadena buscada
print("Hola Mundo mundo mundo".rfind('Mundo')) # Devuelve el ultimo indice de la cadena buscada

var = "100"
var2 = "ABC123"
var3 = "ALPHA"
space = " "

print(var.isdigit()) # Devuelve en booleana si la cadena es de numeros
print(var2.isalnum()) # Devuelve comprobacion del valor de la cadena es alfanumericos
print(var3.isalpha()) # Devuelve comprobracion del valor de la cadena es letras
print(var3.isupper()) # Devuelve comprobacion del valor de la cadena
print(var3.islower()) # Devuelve comprobacion del valor de la cadena
print(var3.istitle()) # Devuelve comprobacion del valor de la cadena
print(space.isspace()) # Devuelve comprobacion del valor de la cadena todos son espacios
print(var3.startswith('AL')) # Devuelve comprobacion si la cadena empieza por "AL"
print(var3.endswith('HA')) # Devuelve comprobacion si la cadena empieza por "HA"

### Mas avanzados

var = "Hola mundo mundo".split() # Separa los valores de una cadena en un lista
var1 = "Hola Mundo,100,Python".split(',') # Separa los valores de una cadena por la ","
cadena = "-".join("Hola Mundo") # Une una cadena por el valor que le pasemos
cad = "---   Hola Mundo  ----".strip('-') # Elimina espacios y caracteres de una cadena
cod = "Hola Mundo".replace('o','0') # Remplazar valores

print(var)
print(var1)
print(cadena)
print(cad)
print(cod)