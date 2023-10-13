import psycopg2

conexion = psycopg2.connect(user='postgres',
                 password='admin',
                 host='127.0.0.1',
                 port='5432',
                 database='test_db')

#Un cursor es un objeto que nos permite ejecutar sentencias
cursor = conexion.cursor()
sentencia = 'INSERT INTO persona(nombre, apellido, e_mail) VALUES(%s, %s, %s)'

#Una tupla de tuplas
valores = (
    ('Marcos', 'Cantu', 'mcantu@mail.com'),
    ('Angel', 'Quintana', 'aquintana@mail.com'),
    ('María', 'Gonzáles', 'mgonzales@mail.com')
)

#Para ejecutar una tupla de tuplas
cursor.executemany(sentencia, valores)
#Para guardar la información pendiente en la BD
conexion.commit()

#Para saber cuantos registros se insertaron
registros_insertados = cursor.rowcount
print(f'Registros insertados: {registros_insertados}')

#Finalmente cierra
cursor.close()
conexion.close()