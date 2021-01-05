###################
#       POO       #
#                 #
#   Autor: Lucho  #
###################

class Coche: # Definir una clase

    # Atributos o Propiedades
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Metodos
    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
    # Metodos Getters y Setters
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

# Crear un objeto / Instanciar la clase
print("########### Coche 1 ############")
coche = Coche()

print(coche.marca, coche.color,)

coche.frenar()
coche.acelerar()
print(coche.getVelocidad())

coche.setColor("Negro")
print(coche.getColor())

coche.setModelo("Audi")
print(coche.getModelo())

print("########### Coche 2 ############")
# Multiples Objetos
coche2 = Coche()

coche2.setColor("Verde")
coche2.setModelo("Gallardo")

print(coche2.marca, coche2.getModelo(), coche2.getColor())