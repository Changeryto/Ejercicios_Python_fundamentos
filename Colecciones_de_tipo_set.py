#No mantienen ningún orden, por tanto no tienen índice
#Los elementos del set son únicos, no pueden duplicarse
#No se pueden modificar los elementos
#Sí podemos agregar elementos o eliminar elementos existentes
#Usan llaves

#Las impresiones pueden ser aleatorias
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

#Revisar el largo
print(len(planetas))

#Revisar si un elemento está en el ser
print("Marte" in planetas)
print("Tierra" in planetas)

#Agregar elementos al set
planetas.add("Tierra")
print(planetas)

#Eliminar elementos de un set
planetas.remove("Tierra") #Tratar de eliminar un elemento inexistente arroja un error
print(planetas)
planetas.discard("Jupiter") #Esto no arroja el error anterior
print(planetas)

#Limpiar el set completamente
planetas.clear()
print(planetas)

#Eliminar el set
del planetas