class Monitor:
    contadorMonitores = 0
    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores += 1
        self.__marca = marca
        self.__tamaño = str(tamaño)
        self.__idMonitor = int(Monitor.contadorMonitores)
        
    #get/set marca
    
    def get_marca(self):
        return self.__marca
    def set_marca(self, nuevaM):
        self.__marca = nuevaM
        
    #get/set tamaño
    
    def get_tamaño(self):
        return self.__tamaño
    def set_tamaño(self, nuevoT):
        self.__tamaño = nuevoT
        
    #get/set id
    
    def get_idMonitor(self):
        return self.__idMonitor
    def set_idMonitor(self, nuevoID):
        self.__idMonitor = nuevoID
        
    def __str__(self):
        return "  ID Monitor: " + str(self.__idMonitor) + "  Marca:  " + self.__marca + "  Tamaño: " + self.__tamaño + " pulgadas"
        
        
"""M1 = Monitor("HP", 22)
print(M1) #Funciona

#print(M1.get_idMonitor)"""