# Conjuntos

c = set()
c.add(1) # Añadir al conjunto
c.add(2)
c.add(3)
c.discard(1) # Descartar del conjunto
print(c)

c2 = c.copy() # Crear copia de conjunto
c2.add(4)
print(c2)

c2.clear() # Limpiar conjunto
print(c2)

######

c1 = {1,2,3}
c2 = {3,4,5}
c3 = {-1,99}
c4 = {1,2,3,4,5}

r1 = c1.isdisjoint(c3) # Disjuntos
r2 = c1.issubset(c4) # Subconjuntos
r3 = c3.issuperset(c1) # Super conjunto, contenedor de otro conjunto
r4 = c1.union(c2) == c4 # Union sin guardado
c1.update(c2) # Union de los dos conjuntos guardado
r5 = c1.difference(c2) # Diferencias
#c1.difference_update(c2) # Guardado de diferencias
r6 = c1.intersection(c2) #
r7 = c1.symmetric_difference(c2)


print(r1)
print(r2)
print(r3)
print(r4)
print(c1)
print(r5)
print(r6)
print(r7)

##########

