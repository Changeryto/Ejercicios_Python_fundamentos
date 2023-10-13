import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

#Un cursor es un objeto que nos permite ejecutar sentencias
cursor = conexion.cursor()
sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, e_mail = %s WHERE id_persona = %s'

valores = ('Juan1', 'Perez2', 'jperez3@mail.com', 1)
cursor.execute(sentencia, valores)
#Para guardar la información pendiente en la BD
conexion.commit()

#Para saber cuantos registros se insertaron
registros_actualizados = cursor.rowcount
print(f'Registros actualizados: {registros_actualizados}')

#Finalmente cierra
cursor.close()
conexion.close()