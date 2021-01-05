###################
#     Modulos     #
#                 #
#   Autor: Lucho  #
###################

#import mi_modulo

#print(mi_modulo.holaMundo("Lucho"))
#print(mi_modulo.calculadora(3,5,True))

#from mi_modulo import holaMundo
#from mi_modulo import calculadora

#print(holaMundo("Lucho"))

"""
# Modulo Fechas
import datetime

print(datetime.date.today())

fecha = datetime.datetime.now()
print(fecha)
print(fecha.year)
print(fecha.month)
print(fecha.day)

fecha_personalizada = fecha.strftime("%d/%m/%Y, %H:%M:%S")
print(fecha_personalizada)
"""

# Modulo de Matematicas

import math

print("Raiz cuadrada de 10: ", math.sqrt(10))
print("Numero pi: ", math.pi)
print("Redondear: ", math.ceil(6.536))
print("Redondear: ", math.floor(6.536))

# Modulo random

import random

print("Numero aleatorio entre 15 y 67: ", random.randint(15, 67))