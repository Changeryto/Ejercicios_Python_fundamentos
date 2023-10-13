from logger_base import logger
import psycopg2 as db
import sys
#import logging

#logger.basicConfig(level=logging.DEBUG)


class Conexion:
    __DATABASE = 'test_db'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __conexion = None
    __cursor = None
    
    @classmethod
    def obtenerConexion(cls):
        if cls.__conexion is None:
            try:
                cls.__conexion = db.connect(host=cls.__HOST,
                                            user=cls.__USERNAME,
                                            password=cls.__PASSWORD,
                                            port=cls.__DB_PORT,
                                            database=cls.__DATABASE)
                logger.debug(f'Conexión exitosa: {cls.__conexion}')
                return cls.__conexion
            except Exception as ex:
                logger.error(f'Error al conectar a la base de datos: {ex}')
                sys.exit()
        else:
            return cls.__conexion
        
    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.obtenerConexion().cursor()
                logger.debug(f'Se abrio el cursor con éxito: {cls.__cursor}')
                return cls.__cursor
            except Exception as ex:
                logger.error(f'Error al obtener cursor: {ex}')
                sys.exit()
        else:
            return cls.__cursor
    
    @classmethod
    def cerrar(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
            except Exception as ex:
                logger.error(f'Error al cerrar cursor: {ex}')
        if cls.__conexion is not None:
            try:
                cls.__conexion.close()
            except Exception as ex:
                logger.error(f'Error al cerrar cursor: {ex}')
        logger.debug('Se han cerrado los objetos conexion y cursor')

if __name__ == '__main__':
    logger.info(Conexion.obtenerCursor())
    Conexion.cerrar()
