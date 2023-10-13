condicion = True
if condicion:
    print("La condición es verdadera")
elif condicion == False:
    print("la condición es falsa")
else:
    print("Condición no reconocida")

#Lo mismo que, en condición acortada, solo si el bloque es sumamente corto y sin elif.

print("Condición verdadera acortada") if condicion else print("Condición falsa acortada")
    
    
numero = int(input("Proporciona un número entero entre 1 y 3: "))
if numero == 1:
    numeroTexto = "numero uno"
elif numero == 2:
    numeroTexto = "numero dos"
elif numero == 3:
    numeroTexto = "numero tres"
else:
    numeroTexto = "Valor fuera de rango"

print("Proporcionado", numeroTexto)