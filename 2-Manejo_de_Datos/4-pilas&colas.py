# Pilas y colas

# Pilas LIFO
#pila = [3,4,5]
#pila.append(6)
#pila.append(7)
#print(pila)
#print(pila.pop())
#print(pila)

# Cola FIFO

from collections import deque

cola = deque()
print(cola)
print(type(cola))
cola = deque(['Luis','Oscar','Pablo'])
cola.append('Maria')
cola.append('Armando')
cola.popleft()
print(cola)