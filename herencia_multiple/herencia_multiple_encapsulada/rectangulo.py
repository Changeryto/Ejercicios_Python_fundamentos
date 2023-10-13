from color import Color
from figura_geometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
    def get_alto(self):
        FiguraGeometrica.get_alto(self)
    def set_alto(self):
        FiguraGeometrica.set_alto(self, alto)
    def get_ancho(self):
        FiguraGeometrica.get_ancho(self)
    def set_ancho(self, ancho):
        FiguraGeometrica.set_ancho(self, ancho)
    def get_color(self):
        Color.get_color(self)
    def set_color(self):
        Color.set_color(self, color)
    def area (self):
        return float(self.__alto * self.__ancho)
    def __str__(self):
        return "\nEl alto es: " + float(self.__alto) + "\nEl ancho es: " + float(self.__ancho) + "\nEl color es: ", str(self.__color)
        
