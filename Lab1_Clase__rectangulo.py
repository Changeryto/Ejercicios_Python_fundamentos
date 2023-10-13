class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcular_area(self):
        return self.base * self.altura
    
base = int(input("Introduce la base: "))
altura = int(input("introduce la altura: "))
area = Rectangulo(base, altura)
print("El area de tu rectángulo es:", area.calcular_area(), "cm³")

