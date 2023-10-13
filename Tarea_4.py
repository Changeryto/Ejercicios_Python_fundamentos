print("Sistema de calificaciones")
calif = float(input("Proporciona un valor entre 0 y 10: "))
if calif <= 10 and calif >= 0:
    if calif >= 9 and calif <= 10:
        nota = "A"
    elif calif >= 8 and calif < 9:
        nota = "B"
    elif calif >= 7 and calif < 8:
        nota = "C"
    elif calif >= 6 and calif < 7:
        nota = "D"
    else:
        nota = "F"
    print(nota)
else:
    print("Valor desconocido")
    
# La función int() trunca el valor introducido, no lo redondea.
print("Sistema de calificaciones v2")
if calif <= 10 and calif >= 0:
    if calif >= 9 and calif <= 10:
        nota = "A"
    elif calif >= 8 and calif < 9:
        nota = "B"
    elif calif >= 7 and calif < 8:
        nota = "C"
    elif calif >= 6 and calif < 7:
        nota = "D"
    else:
        nota = "F"
    print(nota)
else:
    print("Valor desconocido")
    
    