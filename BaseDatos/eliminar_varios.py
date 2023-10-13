import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

#Un cursor es un objeto que nos pejecutar sentenciasermite 
cursor = conexion.cursor()
sentencia = 'DELETE FROM persona WHERE id_persona = %s'

entrada = input("Marca los registros a eliminar separados por comas:    ")
valores = tuple(entrada.split(","))
print(valores)
cursor.executemany(sentencia, valores)

#Para guardar la información pendiente en la BD
conexion.commit()

#Para saber cuantos registros se insertaron
registros_eliminados = cursor.rowcount
print(f'Registros eliminados: {registros_eliminados}')

#Finalmente cierra
cursor.close()
conexion.close()