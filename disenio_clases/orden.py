from producto import Producto #<-- No hace falta hacer esto en Python
class Orden:
    contador_ordenes = 0
    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.__ID_orden = Orden.contador_ordenes
        self.__productos = productos
        
        
    def __str__(self):
        productos_str = ""
        for producto in self.__productos:
            productos_str += producto.__str__() + " \n"
            
        return "Orden: " + str(self.__ID_orden) + "\nProductos: \n" + productos_str
    
    def agregar_producto(self, nuevo_producto):  
        #nuevo = [nuevo_producto]    #Mi solución
        #self.__productos += nuevo
        #Solución del profe:
        self.__productos.append(nuevo_producto)
        
    def calcular_total(self):
        total = 0
        for prod in self.__productos:
            total += prod.get_precio()
        return "Total: $" + str(total)
