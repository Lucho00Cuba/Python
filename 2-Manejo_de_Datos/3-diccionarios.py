# Diccionarios

colores = {'amarillo':'yellow','azul':'blue','verde':'green'}
print(colores['azul'])
print(type(colores))

numeros = {10:'diez',20:'viente'}
print(numeros[10])
numeros[10] = '10-diez'
print(numeros)
del(numeros[10])
print(numeros)

for color in colores:
    print(colores[color])