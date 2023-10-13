import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

#Un cursor es un objeto que nos permite ejecutar sentencias
cursor = conexion.cursor()
sentencia = 'SELECT * FROM persona ORDER BY id_persona DESC'
cursor.execute(sentencia)
registros = cursor.fetchall()
print(registros)

#Finalmente cierra
cursor.close()
conexion.close()