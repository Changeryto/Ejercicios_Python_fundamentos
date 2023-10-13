from Raton import Raton
from Teclado import Teclado
from orden import Orden
from Monitor import Monitor
from DispositivoEntrada import DispositivoEntrada
from computadora import Computadora
#Mundo PC

#Orden 1
monitor1 = Monitor("Acer", "20")
teclado1 = Teclado("USB", "Spectra")
raton1 = Raton("USB", "Logitech")
computadora1 = Computadora("HP", monitor1, teclado1, raton1)
monitor2 = Monitor("Apple", "15")
teclado2 = Teclado("USB-C", "Apple")
raton2 = Raton("USB-C", "Apple")
computadora2 = Computadora("Apple", monitor2, teclado2, raton2)
orden_nueva1 = [computadora1, computadora2]



orden1 = Orden(orden_nueva1)
print(orden1)

M3 = Monitor("Acer", 15)
T3 = Teclado("Interno", "Acer")
R3 = Raton("USB", "Spectra")
computadora3 = Computadora("Nitro 5", M3, T3, R3)

orden1.agregar_computadora(computadora3)
print(orden1)

orden_nueva2 = [computadora3, computadora2]
orden2 = Orden(orden_nueva2)
print(orden2)