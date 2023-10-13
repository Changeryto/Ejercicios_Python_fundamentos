#Una clase es una plantilla de la que se pueden crear objetos
#Las clases en Python son objetos en sí mismos

#Este archivo va a almacenar la clase de persona
#Primera letra en mayuscula
class Persona:
    #pass   #La palabra simplemente pasa la función
    #Todos los métodos dentro de una clase en Python deben recibir como argumento "self", hace referencia al objeto que se está ejecutando en este momento
    #Una clase generalmente está llena de atributos y métodos
    #__init__ es un método
    def __init__(self, nombre, edad):
        self.nombre = nombre  #Self especifíca que pertenece a esta clase, no es una varible definida
        self.edad = edad


#Modificar los valores [No es algo que se hace, se usa como plantilla en vez de ser modificada]
Persona.nombre = "Juan"
Persona.edad = 28

#Acceder a los valores
print(Persona.nombre)
print(Persona.edad)

#Crear un nuevo objeto [Se pueden crear varios según haga falta]
persona = Persona("Karla", 30) #La variable persona apunta a una instancia de la clase Persona
                                #El parámetro de self apunta al objeto que se está ejecutando en este momento
print(persona.nombre)
print(persona.edad)

persona2 = Persona("Carlos", 40)
print(persona2.nombre)
print(persona2.edad)