#Break rompe al completo el ciclo ejecutado
    #Para imprimir solo la primer a
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break # Este break rompe el ciclo for
    
else: #Esta orden se cancela por el brake anterior
    print("Fin ciclo for")
    
print("El resto del programa continua")

    #Para imprimir sólo números pares
for i in range(6):
    if i % 2 == 0:
        print(i)

    #Mismo ejercicio con continue
for i in range(6):
    if i % 2 != 0:
        continue #Este continue se "salta" un paso del ciclo para pasar al siguiente, impidiendo que se ejecute el codigo debajo para este indice
    print(i)