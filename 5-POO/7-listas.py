# Metodos en Listas

lista = [1,2,3,4,5]
lista.append(6) # Agregar valor
lista.clear() # Limpiar lista
print(lista)

l1 = [1,2,3]
l2 = [4,5,6]

l1.extend(l2)
print(l1)
print(l2)

l1= ["Hola mundo","mundo","mundo"]
print(l1.count("mundo"))

print(l1.index("mundo")) # Buscar en Listas

l = [1,2,3]
l.insert(0,0) # Insertar
print(l)
l.pop(0) # Sacar de la lista
l.remove(3) # Eliminar de la lista
l.reverse() # Revertir la lista
print(l)

lista = list("Hola mundo")
lista.reverse()
print(lista)
cadena = "".join(lista)
print(cadena)

lista = [5,-10,3,8,66,9]
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)


