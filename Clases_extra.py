class Persona:
    def __init__(self, n, e, *v, **d):
        self.nombre = n
        self.edad = e
        self.valores = v #Para llamar una tupla, vease el asterisco que indica que el parametro es opcional, para una tupla
        self.diccionario = d #Para llamar un diccionario usese dos asteriscos
    def desplegar(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)
        print("Valores (Tupla:", self.valores)
        print("Valores (Diccionario):", self.diccionario)
        
p1 = Persona("Juan", 28)
p1.desplegar()


p2 = Persona("Carla", 30, 2,4,5)
p2.desplegar()


p3 = Persona("Paola", 33, 4,5,6,7, m="Manzana", p="Pera", j="Jicama")
p3.desplegar()