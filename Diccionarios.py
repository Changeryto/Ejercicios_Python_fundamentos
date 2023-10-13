#Un diccionario consta de una colección de llaves y un valor asociado a cada llave
#Se manejan llaves en lugar de indices
#Podemos hacer cambios en los valores asociados
diccionario = {
    "IDE": "Integrated Development Environment",
    "OOP": "Object Oriented Programing",
    "DBMS": "Database Management System"
    
}
print(diccionario)

#Largo de un diccionario
print(len(diccionario))

#Para acceder a un elemento de un diccionario
print(diccionario["IDE"])
print(diccionario.get("IDE"))

#Modificando valores
diccionario["IDE"] = "Integrated development ..."
print(diccionario)

#Itterar los elementos de un diccionario
for termino in diccionario:
    print(termino)                 #Para acceder a las llaves
for termino in diccionario:
    print(diccionario[termino])    #Para acceder a los terminos de un diccionario

#Para recuperar los valores sin necesidad de los terminos
for valor in diccionario.values(): #Para recuperar cada valor sin sus llaves
    print(valor)

#Comprobar si un elemento existe en el diccionario
print("IDE" in diccionario)
print("VSCode" in diccionario)

#Agregar nuevo elemento al diccionario
diccionario["PK"] = "Primary Key"
print(diccionario)


#Remover un elemento
diccionario.pop("DBMS")
print(diccionario)

#Limpiar el diccionario
diccionario.clear()
print(diccionario)

#Eliminar diccionario
del diccionario