class Computadora:
    contadorComputadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self.__idComputadora = Computadora.contadorComputadoras
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton
        
    
    #get/set idComputadora
    
    def get_idComputadora(self):
        return self.__idComputadora
    def set_idComputadora(self, nuevoID):
        self.__idComputadora = nuevoID
    
    #get/set nombre
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nuevoN):
        self.__nombre = nuevoN
    
    #get/set monitor
    
    def get_monitor(self):
        return self.__monitor
    def set_monitor(self, nuevoM):
        self.__monitor = nuevoM
    
    #get/set teclado
    
    def get_teclado(self):
        return self.__teclado
    def set_teclado(self, nuevoT):
        self.__teclado = nuevoT
        
    #get/set raton
    
    def get_raton(self):
        return self.__raton
    def set_raton(self, nuevoR):
        self.__raton = nuevoR
        
    def __str__(self):
        return "ID COMPUTADORA: " + str(self.__idComputadora) + "\n     NOMBRE: " + self.__nombre + "\n     MONITOR: " + self.__monitor.__str__() + "\n     TECLADO: " + self.__teclado.__str__() + "\n     RATÓN: " + self.__raton.__str__()
    
    
