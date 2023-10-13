from figura_geometrica import FiguraGeometrica
from color import Color


class Cuadrado(FiguraGeometrica, Color): #La llamada super sólo podría llamara a la clase izq.
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    #De ser necesario, se buscan los atributos en clase hija, padres primario y dem+as, y abuela    
    def area(self):
        return self.alto * self.ancho
    