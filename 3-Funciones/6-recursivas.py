# Funciones Recursivas

def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooom!")
    print("Fin de la funcion",num)
cuenta_atras(6)

def factorial(num):
    print("Valor inicial es",num)
    if num > 1:
        num = num * factorial(num - 1)
    print("Valor final es",num)
    return num

print(factorial(5))