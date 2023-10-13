import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

#Un cursor es un objeto que nos permite ejecutar sentencias
cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona WHERE id_persona = %s' # %s es un comodin a sustituir

id_persona = int(input("Proporciona la llave primaria a buscar: ")) #Este es el valor que modifica %s
llave_primaria = (id_persona,) #Así generamos una tupla

cursor.execute(sentencia, llave_primaria)
registros = cursor.fetchone() #ASí regresa sólo un registro
print(registros)



#Finalmente cierra
cursor.close()
conexion.close()