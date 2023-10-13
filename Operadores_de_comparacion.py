a = 4
b = 2
#Todos los operadores de comparacion regresan un valor de tipo booleano

#Operador de comparación
resultado = (a == b) # Lo mismo que resultado = a == b
print(resultado)

#Operador de diferente
resultado = (a != b)
print(resultado)

#Operador de mayor/menor que
resultado = (a > b)
print(resultado)
resultado = (a < b)
print(resultado)

#Operador de mayor/menor o igual que
resultado = (a >= b)
print(resultado)
resultado = (a <= b)
print(resultado)

#Preguntar si es un número par, no olvidar el : que habre el bloque de codigo

if a % 2 == 0:
    print("(a) Este es un numero par")
else:
    print("(a) Este es un numeo impar")
    
#Preguntar si una persona es mayor de edad
edadLimite = 18
edadPersona = 18
if edadPersona >= edadLimite: #Es lo mismo que if(edadPersona > edadLimite):
    print("Es mayor de edad")
else:
    print("Es menor de edad")
    
