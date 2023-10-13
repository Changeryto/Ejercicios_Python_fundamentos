R = 0.082
T = float(input("Temperatura en K: "))
P = float(input("Presión en atm: "))
V = float(input("Volumen en L: "))

n = (P * V) / (R * T)
print(n, "moles")

#v = (R * T * n)/ P
#print(nv, "Litros")

Vol_molar_ox = 0.05 * 22.4
Vol_molar_air = n * 22.4

es = Vol_molar_air * 0.21
print(es, "¿Es cercano a?", Vol_molar_ox)


