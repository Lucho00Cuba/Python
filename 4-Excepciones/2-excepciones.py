# Excepciones

#while(True):
#    try: # <- (probar) Para capturar cualquier error dentro de un bloque de instrucciones
#        n = float(input("Introduce un numero: "))
#        m = 4
#        print("{n}/{m}={r}".format(n=n,m=m,r=n/m))
#    except: # <- Definir codigo excepcional
#        print("Ha ocurrido un error")
#    else: # <- Definir codigo si no ah ocurrido un error
#        print("Todo bien")
#        break # Romper el bluce
#    finally: # <- (finalmente) Para definir el codigo que se ejecuta si existe error o no
#        print("Fin de la iteracion")

#while(True):
#    try:
#        n = float(input("Introduce un numero: "))
#        5/n
#    except TypeError:
#        print("Introducir un numero correcto")
#    except ValueError:
#        print("No se introducir una cadena de texto")
#    except ZeroDivisionError:
#        print("No se puede dividir un numero por cero")
#    except Exception as e: # <<- Ver error
#        print(type(e).__name__) # <<- Ver error 
#    else:
#        print("Bien")
#        break

# Invocar excepciones

def funcion(algo=None):
    #if algo == None:
    try:
        if algo is None:
            raise ValueError("No se permite un valor nulo") # <- Invocar un ValueError
    except ValueError:
        print("Valor Nulo")
funcion()