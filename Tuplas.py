#La tupla mantiene el orden pero los elementos no se pueden modificar
frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)

#El largo de la tupla
print(len(frutas))

#Acceder al elemento con el indice
print(frutas[2])

#Navegación inversa
print(frutas[-1])

#Rango
print(frutas[0:2])

#Para convertir tupla a lista, usar función list("Tupla")
frutasLista = list(frutas)
frutasLista[1] = "Platanito"
print(frutasLista)

#Para convertir lista a tupla, usar función tuple("Lista")
frutas = tuple(frutasLista)
print(frutas)

#Para iterar una tupla
for fruta in frutas:
    print(fruta, end=" ") #Para cambiar el salto de linea (\n) por otro caracter, como un espacio
    
#Para eliminar tupla
del frutas

#print(frutas) arrojaría un error
