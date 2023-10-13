class MiClase:
    
    variable_clase = "Variable clase"
    def __init__(self):
        self.variable_instancia = "Variable instancia"
    
    @staticmethod #Los decoradores agregan cierta funcionalidad
    def metodo_estatico():
        print("Metodo estático")
        # print(variable_clase)  No es posible acceder de esta forma ya que necesitamos especificar a qué variable haceos referencia
        print(MiClase.variable_clase)
        # print(MiClase.variable_instancia) desde el método estático al no haberse creado el objeto no puede accederse de esta forma
        
        #Los métodos estáticos se consultan a la clase en lugar de atribuirse al objeto
        #No reciben ningún parámetro, tampoco podemos acceder al contexto estático (de la clase)
        
    @classmethod  #Sí recibe un parámetro, que se encuentra a nivel de clase
    def metodo_clase(cls): #No recibe self que hace referencia a la clase
        #cls es el típo de la clase en sí mismo
        print("Método de clase: " + str(cls)) #el str nos va a mostrar la cadena asociada a esta variable, el nombre de la clase
        print(cls.variable_clase) #Podemos acceder a las variables de clase con cls
        # print(cls.variable_instacia) No podemos acceder a la variable de instancia desde el contexto
    
    def metodo_instancia(self): #No contienen ningún decorador, se asocia y ejecuta desde los objetos
        self.metodo_estatico()
        self.metodo_clase() #Si es posible acceder a lo métodos o variables de clase, ya que cuando creamos un objeto las variables ya están cargadas
        print(self.variable_clase)
        print(self.variable_instancia) #Observese el self en las variables de clase y de instancia

MiClase.metodo_estatico()
MiClase.metodo_clase()

objeto1 = MiClase()
objeto1.metodo_instancia() #Mandamos a llamar el método estático y clase
#Desde el contexto de instancia podemos acceder al contexto estático
#El contexto estático no puede acceder al contexto dinámico pues no se ha creado

#Los metodos de instancia ya pueden acceder a toda la información