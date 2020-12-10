# Metodos especiales

class Pelicula:
    # Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula", self.titulo)
    # Destructor de clase
    #def __del__(self):
        #print("Se esta borrando la pelicula",self.titulo)
    # Redefinir Metodo String
    def __str__(self):
        return "{n} lanzada en {a} con un duracion de {m} minutos".format(n=self.titulo,a=self.lanzamiento,m=self.duracion)
    # Redefinir Metodo Len
    def __len__(self):
        return self.duracion

p = Pelicula("El Padrino",175,1992)
print(str(p))
print(len(p))

