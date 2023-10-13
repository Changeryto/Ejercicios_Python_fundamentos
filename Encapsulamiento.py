class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  #El doble guión bajo impide el accedo directo al atributo, ya no permite ser modificado directamente
        self.__edad = edad  #Al definirse internamente no será necesario enviar el valor al atributo en la definición del objeto, pero es necesario dar un valor inicial
   
    #Cada que se usen atributos privados será necesario establecer su método ger y set para poder seguir trabajando con ellos    
    def get_nombre(self):
        return self.__nombre  #Este método permite leer la información
    def set_nombre(self, nombre):  #El atributo que reciva el nuevo nombre debe ser diferente al original
        self.__nombre = nombre
    def get_edad(self):
        return self.__edad
    def set_edad(self, edad):
        self.__edad = edad
        
p1 = Persona("Juan", 18)
#print(p1.__nombre) Marca un error
                        #Se puede modificar un valor en la variable cuando los atributos son públicos, desde fuera de la clase.
                        #Se puede definir un atributo como privado para evitar su modificación
print(p1.get_nombre()) #Usar este método permite leer  el atributo
print(p1.get_edad())
#p1.nombre = "Karla" Marca un error
p1.set_nombre("Karla") #Usar este método permite reasignar el atributo
p1.set_edad(20)
print(p1.get_nombre())
print(p1.get_edad())

