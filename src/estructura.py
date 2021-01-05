###################
#     Bucles      #
#                 #
#   Autor: Lucho  #
###################

# Bucle FOR

for i in range(0, 10):
    print("voy por el ",i)

# Ejemplo

print("############ EJEMPLO 2 ################")

#num = input("Introduce un numero del [0-9] ")
num = "5"
num = int(num)

if num >= 0 and num <= 9:
    print(f"La Tabla del {num}")
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")
else:
    print("Introduce un numero correcto")

#####################################################

# Bucle WHILE

contador = 1

while contador <= 100:
    print(f"Estoy en el {contador}")

    contador += 1

##

print("####### EJEMPLO ######")

num_user = int(input(" Introduce un numero: "))

if num_user < 1:
    num_user = 1

print(f"##### Tabla del {num_user}")

contador = 1
while contador <= 10:
    print(f"{num_user} x {contador} = {num_user*contador}")
    contador += 1
else:
    print("Tabla terminada")