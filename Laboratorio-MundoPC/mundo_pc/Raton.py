from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contadorRatones = 0
    def __init__(self, tipo_entrada, marca):
        Raton.contadorRatones += 1
        super().__init__(tipo_entrada, marca)
        self.__idRaton = Raton.contadorRatones
    def __str__(self):
        return "  ID Raton: " + str(self.__idRaton) + "  " + super().__str__()
    
    
"""R1 = Raton("USB-C", "Apple")
print(R1)
R2 = Raton("BT", "Spectra")
print(R2)""" #Funciona