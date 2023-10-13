from logger_base import logger
from psycopg2 import pool
import sys
#import logging

# logger.basicConfig(level=logging.DEBUG)


class Conexion:
    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __MIN_CON = 1  # Mínimo de conexiones
    __MAX_CON = 5
    __pool = None  # Estática a la clase

    @classmethod
    def obtenerPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(cls.__MIN_CON,
                                                       cls.__MAX_CON,
                                                       host=cls.__HOST,
                                                       user=cls.__USERNAME,
                                                       password=cls.__PASSWORD,
                                                       port=cls.__DB_PORT,
                                                       database=cls.__DATABASE)
                logger.debug(f'Creación pool exitosa: {cls.__pool}')
                return cls.__pool
            except Exception as ex:
                logger.error(f'Error al crear el pool de conexiones: {ex}')
                sys.exit()

        else:
            return cls.__pool

    @classmethod
    def obtenerConexion(cls):  # Administra el pool de conexiones
        # Obtener una conexión del objeto pool
        conexion = cls.obtenerPool().getconn()
        logger.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def liberarConexion(cls, conexion):
        # Regresar el objeto conexión al pool
        # cls puede solicitar métodos internos
        cls.obtenerPool().putconn(conexion)  # putconn
        logger.debug(f'Regresamos la conexión al pool : {conexion}')
        logger.debug(f'Estado del pool: {cls.__pool}')

    @classmethod
    def cerrarConexiones(cls):
        # Cerrar el pool y todas sus conexiones
        # AL usarlo se deben asignar desde cero
        cls.obtenerPool().closeall()
        logger.debug(f'Cerramos todas las conexiones del pool: {cls.__pool}')


if __name__ == '__main__':
    # Obtener una conexión a partir del pool
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    #Regresamos las conexiones al pool
    Conexion.liberarConexion(conexion1)
    Conexion.liberarConexion(conexion2)
    #Cerrar el pool
    Conexion.cerrarConexiones()
    #Si intentamos perdir una conexión de un pool enviará el error "conection pool is close"
    #conexion3 = Conexion.obtenerConexion()