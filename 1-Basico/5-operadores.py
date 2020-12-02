# Operadores

# Operadores Relacionales
print("Operadores Relacionales")
v1 = 3 == 2 # Igual que 
v2 = 3 != 2 # Distinto que
v3 = 3 > 2 # Mayor que
v4 = 3 < 2 # Menor que
v5 = 3 >= 4 # Mayor o igual que
v6 = 3 <= 4 # Menor o igual que

l1 = [v1,v2,v3,v4,v5,v6]
print(l1)

# Operadores Logicos
print("Operadores Logicos")
a1 = not True # Negacion
a2 = True and True # Conjuncion (Y)
a3 = True and False
a4 = True or False # Disyuncion (OR)

l2 = [a1,a2,a3,a4]
print(l2)

# Expresiones Aninadas
print("Expresiones Anidadas")

b1 = 10 * 5 - 2**5 >= 20 and not (10 % 5) != 0

"""
Normas de presedencia
1- Parentesis
2- Aritmeticas por sus propias reglas
3- Relacionales
4- Logicos
"""

l3 = [b1]
print(l3)

# Operadores de asignacion
print("Operadores de Asignacion")

valor = 10
valor += 1 # Suma
valor -= 10 # Resta
valor *= 2 # Multiplicacion
valor /= 2 # Division
valor %= 2 # Modulo
valor **= 2 # Potencia

print(valor)

# Ejemplo

n = 0 # Asignacion ede 0 en n
while n < 10: # Expresion Relacional
    if (n % 2) == 0: # Expresion Aritmetica
        print(n,'es un numero par')
    else:
        print(n,'es un numero impar')
    n += 1 # Expresion Aritmetica
