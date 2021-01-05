###################
#      Listas     #
#                 #
#   Autor: Lucho  #
###################

peliculas = "Batman"
peliculas = ["Batman", "Spiderman", "Iron Man"] # -> Definiendo Lista
cantantes = list(("2pac", "drake", "xxxtentancion")) # -> Defiendo una lista
años = list(range(2020, 2025))
variada = ["Lucho", 5, 1.1, True, "Linux"]

print(peliculas)
print(cantantes)
print(años)
print(variada)

# Añadir elementos a listas

cantantes.append("Walker")
print(cantantes)

# Recorrer lista

for i in peliculas:
    print(f"{peliculas.index(i)+1}. {i}")

#####################################################################