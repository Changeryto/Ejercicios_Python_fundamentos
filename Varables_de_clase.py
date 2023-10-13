class MiClase:
    variable_clase = "Variable de clase"
    def __init__(self, variable_insancia):
        self.variable_insancia = variable_insancia #Variable de instancia, asociada al objeto a crear, cada una con su valor
        
        
print(MiClase.variable_clase)
#print(MiClase.variable_instancia) #Va a marcar un error porque al no crearse un ojeto no se ha creado la variable

objeto1 = MiClase("Variable instancia")
MiClase.variable_instancia = "Modificando variable de instancia" #Cuando se modifica es que se asocia el valor a la clase en sí misma
print(MiClase.variable_instancia) #valores distintos
print(objeto1.variable_insancia) #valores distintos

print(objeto1.variable_clase)
#Podemos acceder a las variables de clase desde la clase o el objeto
print(MiClase.variable_clase) #Mismos valores
#Los objetos pueden acceder a las variables de clase
#Las clases no pueden acceder a variables de instancia que no se les den

objeto1.variable_clase = "Modificando variable de clase"
print(objeto1.variable_clase) #Solo estamos modificando el valor para este objeto, se crea una nueva variable asociado al objeto
print(MiClase.variable_clase)

objeto2 = MiClase("Nuevo valor de instancia")
print(objeto2.variable_clase) #Usa el mismo valor de la clase

objeto3 = MiClase("tercer objeto")
print(objeto3.variable_clase)
MiClase.variable_clase = "Cambio desde la clase" #Afecta a los objetos que no hayan definido su propia vaiable de clase

print(objeto1.variable_clase)
print(objeto2.variable_clase)
print(objeto3.variable_clase)

#Los objetos creados a partir de la clase van a consultar las variables de calse a las clases a menos que hayan definido su propio valor para la variable de clase