class Orden:
    contadorOrdenes = 0
    
    def __init__(self, lista):
        Orden.contadorOrdenes += 1
        self.__lista_computadoras = lista
        self.__idOrden = Orden.contadorOrdenes

    def agregarComputadora(self, computadora):
        self.__lista_computadoras.append(computadora)
        
    def agregar_computadora(self, nuevaC):
        self.__lista_computadoras.append(nuevaC)
        
    def get_computadoras(self):
        return self.__lista_computadoras
    
    def set_computadora(self, nuevaC):
        self.__lista_computadoras = nuevaC
        
    def get_idOrden(self):
        return self.__idOrden
    
    def set_idOrden(self, nuevoID):
        self.__idOrden = nuevoID
        
    def __str__(self):
        computadoras_str = ""
        for computadora in self.__lista_computadoras:
            computadoras_str += computadora.__str__() + "\n"
            
        return "Orden: " + str(self.__idOrden) + "\nProductos: \n" + computadoras_str