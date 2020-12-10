# Encapsulacion de atributos y metodos

class Ejemplo:
    __atributo_privado = "Soy un atributo privado"

    def __metodo_privado(self):
        print("Soy un metodo privado")

    def atributo_publico(self):
        return self.__metodo_privado
    
    def  metodo_publico(self):
        return self.__metodo_privado()

e = Ejemplo()
#print(e.__atributo_privado)
#print(e.__metodo_privado())
print(e.metodo_publico())