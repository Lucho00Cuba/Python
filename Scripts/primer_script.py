# Scripts de Pruebas
import sys

v = "Hola Mundo"
n = 10

# Salidas
print("Hola People,",v,"ya somos",n)
print("Hola People, {} ya somos {}".format(v,n))
print("Hola People, {texto} ya somos {numero}".format(texto=v,numero=n))

comand = "ayuda"
ayuda = "Comando de ayuda"
print("{c}{h:>60}".format(c=comand, h=ayuda))

# Recibiendo argumentos
if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])
    for r in range(repeticiones):
        print(texto)
else:
    print("Error, introduce los argumentos correctamente")
    print("Ejemplo: ./script.py 'mensaje' #")