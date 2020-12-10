# Clases y Objetos

class Galleta: # <- La clase es un molde para objetos
    chocolate = False
    def __init__(self):
        print("Creando un  galleta")
una_galleta = Galleta()

print(type(una_galleta))
una_galleta.sabor = "Salado"
una_galleta.color = "Negro"
print(una_galleta.sabor)

g = Galleta()
print(g.chocolate)

