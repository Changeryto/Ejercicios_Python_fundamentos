#Existen dos tipos de archivos, los de texto (.txt), y los binarios que son cualquier otra extensión

"""archivo = open("prueba.txt", "w") #Se abre un archivo en esta ruta con tal nombre o se crea si no existe"""

#r : modo por default, abre un archivo para lectura pero erra si no existe
#a : anexar, abre un archivo para append, crea uno si no existe
#w : write, abre un archivo para escribir, crea uno si no existe
#x : create, crea el archivo especificado y lanza un error si ya existe

#t : texto, por default
#b : binario, otras extensiones

#n+ : El más significa que lo abrímos para modificarlo y leerlo
"""archivo.close() #Es importante poner esta linea al fnal de nuestro código"""

try:
    archivo = open("Prueba.txt", "w")
    archivo.write("Agregamos info al archivo")
    archivo.write("\nAdios")
except Exception as e:
    print(e)
finally:
    archivo.close()
    #archivo.write("unu") #Esto mandaría un error ya que el recurso ya está cerrado