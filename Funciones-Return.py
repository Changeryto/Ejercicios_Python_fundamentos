def suma(a, b):
    return a + b #return palabra reservada para regresar un valor

print("El resultado es: ", suma(5, 3)) #Esta función otorga el valor regresado


def suma(a = 0, b = 0): #Esto asigna valores por default que no se definen en los parámetros
    return a + b 

print("El resultado es: ", suma()) #Esta función otorga el valor regresado


def suma(a = 0, b = 0): #Esto asigna valores por default que no se definen en los parámetros
    return a + b 

print("El resultado es: ", suma(2, 3)) #Este argumento sobreescribe los valores por default