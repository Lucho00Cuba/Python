# Funciones con retorno de valores

def test():
    return "Una cadena retornada"
    print("Hola Mundo")

print(test())

# Lista

def test():
    return [1,2,3,5]

l = test()
print(l[-1])

# Tupla

def test():
    return "Una cadena",20, [1,2,3]
c,n,l = test()
print(c)
print(n)
print(l)
