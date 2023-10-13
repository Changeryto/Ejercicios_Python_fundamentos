class Persona:                          #Se hereda de la clase object, no hace falta especificarlo
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):      #Para emprimir los valores de los atributos, __str__ sobreescribe al método print
        return "Nombre: " + self.nombre + "  Edad: " + str(self.edad)     #Usar concatenación "+ str(x)"
        
class Empleado(Persona):   #IMPORTANTE     #Esta clase hereda de la clase persona (clase padre en este caso), un solo objeto que hereda los valores
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)             #super() permite acceder a los atributos o métodos de la clase padre
        self.sueldo = sueldo
        
    def __str__(self):
        return super().__str__() + "  Sueldo: " + str(self.sueldo)
    
persona = Persona("Juan", 28)       #Sin el método __str__, print imprime la ubicación en RAM
print(persona)

empleado = Empleado("Karla", 30, 500.00)
print(empleado)

empleado.nombre = "Karla Ivone"     #Estamos sobreescribiendo los atributos desde la clase hija
empleado.sueldo = 1000.00
print(empleado)