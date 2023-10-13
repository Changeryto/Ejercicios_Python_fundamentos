import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

#Un cursor es un objeto que nos permite ejecutar sentencias
cursor = conexion.cursor()
sentencia = 'DELETE FROM persona WHERE id_persona = %s'

#valores = (12,)
entrada = input("Proporciona la PK a eliminar: ")
valores = (entrada,)
cursor.execute(sentencia, valores)
#Para guardar la información pendiente en la BD
conexion.commit()

#Para saber cuantos registros se insertaron
registros_eliminados = cursor.rowcount
print(f'Registros eliminados: {registros_eliminados}')

#Finalmente cierra
cursor.close()
conexion.close()