from Raton import Raton
from Teclado import Teclado
from Monitor import Monitor
from DispositivoEntrada import DispositivoEntrada
from computadora import Computadora

R1 = Raton("USB", "HP")
T1 = Teclado("USB", "Spectra")
M1 = Monitor("HP", 22)
C1 = Computadora("Nitro 10", M1, T1, R1)
print(C1)