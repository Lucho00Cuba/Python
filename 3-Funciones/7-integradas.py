# Funciones Integradas

# Convertir una cadena en un entero
n = int("10")
print(type(n))

# Concatenar un a cadena con numeros
c = "Un texto y un numero" + str(10) + " " + str(3.14)
print(c)

# Convertir enteros 
print(bin(10)) # Binario
print(hex(10)) # Hexadecimal

# Covertir a enteros 
print(int('0b1010',2)) # Binario > Entero
print(int('0xa',16)) # Hexadecimal > Entero

##############
print(abs(-10)) # Valor Absoluto
print(round(5.5)) # Redondear
print(eval("2+5")) # Evaluar
print(len("Hola Mundo")) # Longitud

help()