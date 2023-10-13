# Una lista es un conjunto de elementos que podemos almacenar en una sola varible

#Funcioones indispensables: pop(x) ~ del lista[x], remove("listado") y insert(x, "listado"), append("listado") 

nombres = ["Juan", "Carla", "Ricardo", "Maria"] #Las operaciones podrían solicitar el índice
print(nombres)
#Conocer el largo de la lista, la función len() regresa un conteo entero de un objeto
print(len(nombres))
#Para acceder sólo a un elemento de la lista, lista[x], accede al indice x de la lista
print(nombres[0]) #Proporcionar un indice fuera de rango genera un IndexError
#También se puede proporcionar indices negativos para viajar en la lista
print(nombres[-1]) #Para acceder al último elemento de la lista
print(nombres[-2])
#Podemos indicar los elementos a recuperar de otra forma

#Imprimir rango
print(nombres[0:2]) #Esta notación recupera el primer elemento y hasta antes del segundo elemento
#Imprimir los elementos de inicio hasta el indice proporcionado
print(nombres[:3]) #Similar al anterior, descarta el último elemento
#Imprimir los elementos hasta el final desde el indice proporcionado
print(nombres[1:]) #Inicia los elementos desde el primer elemento hasta el último existente
#Cambiar los elementos de una lista
nombres[3] = "Ivonne"
print(nombres)

#Iterar la lista
for nombre in nombres:
    print(nombre)
    
#Si un elemento existe dentro de la lista
if "Karla" in nombres:
    print("Karla existe en la lista")
else:
    print("El elemento buscado no existe en la lista")
    
    
#Agregar un nuevo elemento a la lista
nombres.append("Lorenzo")
print(nombres)

#Agregar nuevo elemento en el indice proporcionado
nombres.insert(1, "Octavio") #Esto lo inserta exactamente antes del indice 1
print(nombres)

#Remover un elemento de la lista

nombres.remove("Octavio")
print(nombres)

#Remover el último elemento de la lista
nombres.pop()
print(nombres)

#Remover el indice indicado de la lista
del nombres[0]
print(nombres)

#Limpiar todos los elementos de la lista
nombres.clear()
print(nombres)

#Eliminar la variable de la lista
del nombres #Esto indefine la lista de la memoria