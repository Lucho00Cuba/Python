
# Funciones 

_Las funciones en un conjunto de intrucciones agrupadas bajo un nombre en concreto que pueden reutilizarse invacando a la funcion tantas veces como sea necesario_

```python
def NombreDeMiFuncion(parametros): # -> Definiendo Funcion
    # Conjunto de instrucciones

NombreDeMiFuncion(parametros) # -> Llamando a la funcion

#### Ejemplo Real ####

def suma(a, b):
    return a+b

resultado = suma(1,1) # -> Almacenamos en la variable resultado lo que nos devuelve la funcion
print(resultado)
```

### Parametros

```python
def mostrarNombre(name):
    print(f"Tu nombre es {name}")

nombre = input("Introduce tu Nombre: ")
mostrarNombre(nombre)
```

### Parametros Opcionales

```python
def getEmpleado(name, dni=None):
    print("EMPLEADO")
    print(f"Nombre: {name}")
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Lucho", 123)
getEmpleado("Linux")
```

### Funciones dentro de funciones

```python
def getNombre(name):
    texto = f"El nombre es: {name}"
    return texto

def getNick(nick):
    texto = f"El nick es: {nick}"
    return texto

def devuelveTodo(name, nick):
    texto = getNombre(name) + "\n" + getNick(nick)
    return texto

#print(getNombre("Lucho"), getNick("Linux"))
print(devuelveTodo("Lucho","Linux"))
```

### Funciones Lambdas

_Funciones anonimas_

```python
year = lambda year: f"El año es {year}"

print(year(2032))
```

### Funciones Predefinidas

_Pequeña lista de algunas de ellas_

```python
print() # -> Imprime un dato
type() # -> Detectar el tipo de dato
int() # -> Cambia a entero un dato
str() # -> Cambia a cadena de texto un dato
float() # -> Cambia a un numero florante un dato
del() # -> Eliminar un dato
len() # -> Saber longitud de un dato
find() # -> Buscar un dato
```

[Funciones](../src/funciones.py)