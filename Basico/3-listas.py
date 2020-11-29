# Listas

n1 = [1,2,3,4,]
d1 = [5, "Lucho", 10, 1.1, "Linux_Cuba"]
pares = [2,4,6,8,10]
pares[3] = 5
pares.append(12)
letras = ['a','b','c','d']
letras[:3] = ['A','B','C']
letras[:3] = []

print(n1)
print(d1)
print(d1[1])
print(pares)
print(letras)
print(len(letras))

# Listas Anidadas

a = [9,8,7]
b = [1,2,3]
r = [a, b]
print(r)
print(r[0][0])