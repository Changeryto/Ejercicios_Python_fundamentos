import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

#Un cursor es un objeto que nos permite ejecutar sentencias
cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona WHERE id_persona IN %s' # El IN nos permite seleccionar varias llaves primarias



entrada = input("Proporciona las llaves a buscar separadas por comas: ")
tupla = tuple(entrada.split(',')) #Split para que cada un de los elementos separados por coma (en este caso) nos genere un nuevo valor
                                #Se convierte en una tupla
print(tupla)
llaves_primarias = (tupla,) #Debe ser convertido a una tupla de tuplas


cursor.execute(sentencia, llaves_primarias)
registros = cursor.fetchall() #ASí regresa todos los registros


for registro in registros:
    print(registro)

#Finalmente cierra
cursor.close()
conexion.close()