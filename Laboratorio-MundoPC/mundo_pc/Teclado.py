from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contadorTeclados = 0
    def __init__(self, tipo_entrada, marca):
        Teclado.contadorTeclados += 1
        super().__init__(tipo_entrada, marca)
        self.__idTeclado = Teclado.contadorTeclados
    
    def __str__(self):
        return "  ID Teclado: " + str(self.__idTeclado) + "  " + super().__str__()
    
    
"""T1 = Teclado("USB", "HP")
print(T1)""" #Funciona