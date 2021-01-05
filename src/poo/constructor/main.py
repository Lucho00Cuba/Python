
from coche import Coche

carro = Coche("Negro", "Ferrari", "Aventador", 150, 200, 4)
carro1 = Coche("Verde", "Seat", "Panda", 240, 200, 4)
carro2 = Coche("Azul", "Citroen", "Xara", 100, 180, 4)
carro3 = Coche("Rojo", "Mercedes", "Clase A", 350, 400, 4)

print(carro.getall())
print(carro1.getall())
print(carro2.getall())
print(carro3.getall())

# Detectar Tipado

if type(carro3) == Coche:
    print("Es un objeto Correcto")
else:
    print("No es un objeto")

print(carro.soy_publico)
print(carro.getPrivado())
