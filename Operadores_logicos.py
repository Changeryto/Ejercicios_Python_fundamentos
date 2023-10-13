#Los operadores lógicos nos permiten comparar 2 expresiones booleanas
a = 5
#Si esta variable está dentro de un rango entre 0 y 5
valor_min = 0
valor_max = 5
dentro_de_rango = (a >= valor_min and a <= valor_max) #El operador and agrega otra condicional obligatoria (n)
if (dentro_de_rango): #En un If/Else, las variables True activarán un bloque de código, las False no, no es necesario escribir el comparador
    print("dentro de rango")
else:
    print("fuera de rango")
    
    
    
    
vacaciones = True
diaDescanso = False
if(vacaciones or diaDescanso): #El operador or agrega otra condicional posible (u)
    print("Puedes ir al parque")
else:
    print("tienes deberes que hacer")
    
print((not(vacaciones))) #El operador not invierte el valor booleano (**c)
