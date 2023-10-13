from cuadrado import Cuadrado
cuadrado = Cuadrado(4, "azúl")
print(cuadrado.area())
print(cuadrado.color)

#Este método refiere al orden de las clases de las que hereda la clase hija
print(Cuadrado.mro())