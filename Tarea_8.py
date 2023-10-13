class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    def __str__(self):
        return "Color: " + self.color + "  Ruedas: " + self.ruedas
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return super().__str__() + "  Velocidad: " + str(self.velocidad) + "km/h"
    
class Bicicleta(Coche):
    def __init__(self, color, ruedas, velocidad, tipo):
        super().__init__(color, ruedas, velocidad)
        self.tipo = tipo
    def __str__(self):
        return super().__str__() + "  Tipo: " + self.tipo
    

vehiculo = Vehiculo("Verde", "Diagonal")
print(vehiculo)

coche = Coche("Negro", "Radial", 200)
print(coche)

bicicleta = Bicicleta("Rojo", "Drifter", 20, "BMX")
print(bicicleta)