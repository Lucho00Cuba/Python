###################
#  Primer Modulo  #
#                 #
#   Autor: Lucho  #
###################

def holaMundo(nombre):
    return f"Hola que tal estas, {nombre}"

def calculadora(num1, num2, basicas=False):

    s = num1 + num2
    r = num1 - num2
    m = num1 * num2
    d = num1 / num2
    cadena = ""

    if basicas !=False:
        cadena += "Suma: " + str(s)
        cadena += "\n"
        cadena += "Resta: " + str(r)
        cadena += "\n"
    else:
        cadena += "Multiplicacion: " + str(m)
        cadena += "\n"
        cadena += "Division: " + str(d)
        
    return cadena
