###################
#  Concatenacion  #
#                 #
#   Autor: Lucho  #
###################

nombre = "Lucho"
nick = "Linux Cuba"
web = "https://lucho00cuba.github.io"

print(nombre + " " + nick + " - " + web) # -> Metodo 1
print(f"{nombre} {nick} - {web}") # -> Metodo 2
print("Mi nombre es {}, ni nick es {} y mi web es {}".format(nombre, nick, web)) # -> Metodo 3
print("Mi nombre es {no}, ni nick es {n} y mi web es {w}".format(no=nombre, n=nick, w=web)) # -> Metodo 4