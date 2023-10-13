from conexion import Conexion
from logger_base import logger

class CursorDelPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None
        
    def __enter__(self):
        logger.debug(f'Inicio del método __enter__')
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()
        return self.__cursor
        
    def __exit__(self, exception_type, exception_value, exception_traceback):
        logger.debug(f'Se ejecuta el método __exit__()')
        if exception_value:
            self.__conn.rollback()
            logger.debug(f'Ocurrió una excepción: {self.__conn}')
        else:
            self.__conn.commit()
            logger.debug(f'Commit de la transacción')
        
        self.__cursor.close
        Conexion.liberarConexion(self.__conn)
            