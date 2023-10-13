class Persona(object):
    def __init__(self, nombre):
        self.__nombre = nombre
    #Este método permite sobrecargar el "+" para agregar una nueva funcionalidad
    def __add__(self, otro):    
        return self.__nombre + " " +otro.__nombre
    #Este método permite sorecargar el "-"     
    def __sub__(self, otro):
        return "Operación no resta soportada"
    def __mul__(self, otro):
        return "Multiplicador sorecargado"
    def __truediv__(self, otro):
        return "Divisor sobrecargado"
    def __floordiv__(self, otro):
        return "Divisor de entero // sobrecargado"
    def __mod__(self, otro):
        return "Modulador sobrecargado"
    def __pow__(self, otro):
        return "Exponencial sobrecargado"
    def __lt__(self, otro):
        return "< sobrecargado"
    def __gt__(self, otro):
        return "> sobrecargado"
    def __le__(self, otro):
        return "<= sobrecargado"
    def __ge__(self, otro):
        return ">= sobrecargado"
    def __eq__(self, otro):
        return "== sobrecargado"
    def __ne__(self, otro):
        return "!= sobrecargado"
        
        
    #Operadores unarios, que sólo tienen un objeto a la derecha
    def __neg__(self, otro):
        return "Unario +"
    def __pos__(self, otro):
        return "Unario -"
    def __invert__(self, otro):
        return "Unario ~"
        
p1 = Persona("Juan")
p2 = Persona("Karla")

print(p1 + p2)

print(p1 - p2)