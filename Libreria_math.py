import math

#Constantes matemáticas

print("pi:", math.pi)

print("e:", math.e)

print("tau:", math.tau)

print("Infinito:", math.inf)

print("También infinito:", float("inf"))

print("No un número:", math.nan)

print("También nan:", float("nan"))

#Métodos matemáticos

print("Raiz cuadrada de 10:", math.sqrt(10))

print("Logaritmo natural de 5:", math.log(5))

print("logaritmo base 10 de 72:", math.log10(72))

print("Logaritmo base 7 de  70:", math.log(70, 7))

print("Loagritmo natural de 5, más 1:", math.log1p(5))

print("Exponente 10 de e:", math.exp(10))

print("Potencia de 10 ^10:", math.pow(10, 10))

print("Redondear al techo 10.548:", math.ceil(10.548))

print("Redondear al suelo 10.548:", math.floor(10.548))

print("Truncar 10.548:", math.trunc(10.548))

print("Copiar el signo de -2 para ponerselo al 0:", math.copysign(0, -2))

print("Obtener el valor absoluto de -3:", math.fabs(-3))

print("Obtener el factorial de 7:", math.factorial(7))

print("Combinaciones de 10 objetos tomados de entre 50 objetos:", (math.factorial(50) / (math.factorial(10) * math.factorial(50-10))))

print("Obtener el módulo de 7 / 3:", math.fmod(7, 3))

print("División entera de 7 / 3", (7 // 3))

print("También el módulo de 7 / 3:", math.remainder(7, 3))

print("Obtener una tupla que divida la parte entera y la parte decimal de 7.5:", math.modf(7.5))

print("Obtener el máximo común divisor de 13 y 64:", math.gcd(13, 64))

print("Bool de si 2.5 es finito:", math.isfinite(2.5))

print("Bool de si 2.5 es infinito", math.isinf(2.5))

print("Bool de si math.nan es un not a number:", math.isnan(math.nan))

print("Bool para comprobar de si math.sqrt(2)**2 y 2 son metemáticamente prácticamente iguales", math.isclose(math.sqrt(2)**2, 2))

print("Bool para comprobar de si 2.5 y 2.51 son metemáticamente prácticamente iguales, con 2 digitos iguales", math.isclose(2.5, 2.51, abs_tol=2))

#Más preciso que math.exp(3) - 1
print("Exponente 3 de e, menos uno:", math.expm1(3))

#Funciones trigonométricas, en radianes

print("Seno de pi/2:", math.sin(math.pi/2))

print("Coseno de pi/2:", math.cos(math.pi/2))

print("Tangente de pi/2:", math.tan(math.pi/2))

print("Arcoseno de 1:", math.asin(1))

print("Arcocoseno de 1:", math.acos(1))

print("Arcotangente de 1:", math.atan(1))

print("Convertir pi radianes a grados:", math.degrees(math.pi))

print("Converitr 60 grados a radianes:", math.radians(60))

print("Norma eucidia para determinar la distancia entre dos puntos que delimitan un vector, 3 de ancho y 4 de alto:", math.hypot(3, 4)) 

print("Ángulo que forma el vector con el eje horizontal, 4 en eje y, 3 en eje x:", math.atan2(4, 3))

#Funciones hiperbólicas

print("Seno hiperbólico de 0:", math.sinh(0))

print("Coseno hiperbólico de 0:", math.cosh(0))

print("Tangente hiperbólica de 0:", math.tanh(0))

#Funciones probabilísticas

print("Funcion de error de Gauss de pi:", math.erf(math.pi)) #Función de distribución acumulada de la distribución normal

print("Función complementaria (1 - erf(x)) de 2:", math.erfc(2))

print("Función gamma (n -1)!, o factorial generalizado para números reales, en este caso de 2.5:", math.gamma(2.5))

