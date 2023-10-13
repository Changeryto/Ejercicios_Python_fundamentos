from empleado import Empleado
from gerente import Gerente

def imprimir_detalles(tipo_padre):
    print(tipo_padre)
    print(type(tipo_padre), end="\n\n")
    if isinstance(tipo_padre, Gerente): #Pregunta si es del tipo gerente para  ejecutar el próximo código
        print(tipo_padre.departamento)
    
empleado = Empleado("Juan", 1000.00)
imprimir_detalles(empleado)

#Ahora en lugar de llamar a un método padre llama a un método hija
empleado = Gerente("Karla", 2000.00, "Sistemas")
imprimir_detalles(empleado)
