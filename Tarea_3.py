print("Calcular el area y perimetro de un rectangulo")
alto = int(input("Proporciona el alto: "))
ancho = int(input("Proporciona el ancho: "))
area = alto * ancho
perimetro = (alto * 2) + (ancho * 2)
print("Area: " + str(area))
print("Perimetro: " + str(perimetro))

print("El mayor de dos numeros")
a = float(input("Proporciona el numero 1: "))
b = float(input("Proporciona el numero 2: "))
c = a > b
if(c):
    print("El numero mayor es: ", a)
else:
    print("El numero mayor es: ", b)