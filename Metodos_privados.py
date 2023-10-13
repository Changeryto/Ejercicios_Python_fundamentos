class Persona:
    def __init__(self, nombre, apellido_paterno, apellido_materno):
        self.nombre = nombre                            #Atributo público, modificable
        self._apellido_paterno = apellido_paterno       #Atributo parcialmente privado, modificable sin get
        self.__apellido_materno = apellido_materno      #Atributo privado, requiere get y set
        
    def metodo_publico(self): #Este método público permite mandar a llamar al método privado
        self.__metodo_privado()
        
    def __metodo_privado(self):       #El doble guión bajo hace al método privado, require su acceso desde un método público
        print(self.nombre)
        print(self._apellido_paterno)
        print(self.__apellido_materno)
    
    def get_apellido_paterno(self):
        return self._apellido_paterno
    def set_apellido_paterno(self, apellido_paterno):
        self._apellido_paterno = apellido_paterno
    
    def get_apellido_materno(self):
        return self.__apellido_materno
    def set_apellido_materno(self, apellido_materno):
        self.__apellido_materno = apellido_materno
    
    
        
p1 = Persona("Juan", "Lopez", "Perez")
#p1.__metodo_privado() Marca un error
p1.metodo_publico()

print(p1.nombre)        #Observese que no se llama a un método si no a un atributo por lo que no se deve colocar paréntesis
print(p1._apellido_paterno) #Se debería evitar el uso de este acceso en lugar de get o set, es una sugerencia y no una orden
print(p1.get_apellido_materno())