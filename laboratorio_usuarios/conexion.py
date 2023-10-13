from psycopg2 import pool
from logger_base import logger
import sys


class Conexion:
    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __MIN_CON = 1  # Mínimo de conexiones
    __MAX_CON = 5
    __pool = None

    @classmethod
    def obtenerPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(cls.__MIN_CON, cls.__MAX_CON, host=cls.__HOST,
                                                       user=cls.__USERNAME, 
                                                       password=cls.__PASSWORD, 
                                                       port=cls.__DB_PORT, 
                                                       database=cls.__DATABASE)
                logger.debug(f'Creación pool exitosa: {cls.__pool}')
                return cls.__pool
            except Exception as ex:
                logger.error(f'Error al crear pool de conexions: {ex}')
                sys.exit
        else:
            return cls.__pool
        
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        logger.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion
    
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        logger.debug(f'Regresamos la conexión al pool: {conexion}')
        logger.debug(f'Estado del pool: {cls.__pool}')
    
    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()
        logger.debug(f'Todas las conexiones al pool cerradas; {cls.__pool}')
