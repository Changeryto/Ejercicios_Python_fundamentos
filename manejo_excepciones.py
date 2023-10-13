
from excepciones_creadas_numeros_idénticos import NumerosIdenticosException


resultado = None

#Si las variables se definen en el bloque try, se destruyen al finalizar el bloque, s necesitas usarla fuera entonces declara la variable por fuera
try:
    a = float(input("Dividendo: "))
    b = float(input("Divisor: "))
    if a == b:
        raise NumerosIdenticosException(": Números idénticos") #La palabra raise lanza la excepción
    resultado = a / b
except ZeroDivisionError as e:
#except Exception as e:
    print("Ocurrió un error con ZeroDivisionError", e) #Hace que ya no termine de manera anormal
    print(type(e))
except TypeError as e:
    print("Ocurrió un error con TypeError", e) #Hace que ya no termine de manera anormal
    print(type(e))
except ValueError as e:
    print("Ocurrió un error con ValueError", e)
    print(type(e))
#Al colocar la class Exception, de mayor jerarquía, el resto puede ejecutarse antes de llegar a ella y se puede ser más específico.
except Exception as e:
    print("Ocurrió un error genérico con Exception", e) #Hace que ya no termine de manera anormal
    print(type(e))
#Si no hay excepciones se puede usar un bloque else
else:
    print("No hubo ninguna excepción")    
#Este bloque se ejecuta con o sin errores, incluso en casos donde ocurre una excepción no procesada que acaba el programa
finally:
    print("Fin del manejo de excepciones")

    
print("Resultado: ", resultado)
print("Continuamos...")

#Aunque ocurre un error, el programa puede continuar

