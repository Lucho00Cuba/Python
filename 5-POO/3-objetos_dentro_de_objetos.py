# Objetos dentro de objetos

class Pelicula:
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la pelicula",self.titulo)
    
    def __str__(self):
        return "{n} lanzada en {a} con un duracion de {m} minutos".format(n=self.titulo,a=self.lanzamiento,m=self.duracion)

class Catalogo:
    peliculas = []
    
    def __init__(self,peliculas=[]):
        self.peliculas = peliculas

    def agregar(self,p):
        self.peliculas.append(p)
    
    def mostrar(self):
        for p in self.peliculas:
            print(p)

p = Pelicula("El Padrino",175,1972)
c = Catalogo([p])
c.mostrar()
c.agregar(Pelicula("El Padrino 2",202,1974))
c.mostrar()
