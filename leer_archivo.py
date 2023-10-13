#Sólo en windows debemos usar esta doble diagonal inversa
#Ya que un \ es un signo de escape
#En derivados de UNIX no hace falta, usa la diagonal normal
archivo = open("C:\\Programación ExL\\Python\\Fundamentos\\Prueba.txt", "r")
#print(archivo.read()) #Así mandamos a imprimir el archivo

"""
#Si leemos el archivo y llegamos al final entonces ya no hay más información qué leer
#Leer algunos caracteres, en este caso 5
print(archivo.read(5))
print(archivo.read(3))

#Leer lineas completas del archivo
print(archivo.readline())
print(archivo.readline())
"""

"""
#Iterar
for linea in archivo:
    print(linea)
"""
"""
#Leer todas las líneas
print(archivo.readlines())
"""

#acceder a una linea de la lista, podemos proporcionar el índice
print(archivo.readlines()[1])


#Cómo copiar un archivo
### Esto no fuciona si hay caracteres especiales en el documento
archivo2 = open("copia.txt", "a") #"w" sobreescribiría, "a" anexaría

archivo2.write(archivo.read())


#print(archivo2.read)

archivo.close()
archivo2.close()

