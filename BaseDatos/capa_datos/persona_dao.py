from persona import Persona
from conexion import Conexion
from logger_base import logger

class PersonaDao:
    '''
    DAO (Data Acces Object) 
    CRUD: Create(Insert)-Read-Update-Delete entidad persona
    '''
    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona(nombre, apellido, e_mail) VALUES(%s, %s, %s)'
    __ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'
    __ACTUALIZAR = 'UPDATE persona SET nombre=%s, apellido=%s, e_mail=%s WHERE id_persona=%s'
    
    @classmethod
    def seleccionar(cls):
        cursor = Conexion.obtenerCursor()
        logger.debug(cursor.mogrify(cls.__SELECCIONAR)) #Imprime el logging en la BD
        cursor.execute(cls.__SELECCIONAR)
        registros = cursor.fetchall()
        personas = []
        for registro in registros:
            persona = Persona(registro[0], registro[1], registro[2], registro[3])
            personas.append(persona)
        Conexion.cerrar()
        return personas
    
    @classmethod
    def insertar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_e_mail())
            cursor.execute(cls.__INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount ################ Sin Paréntesis es variable, no método
        except Exception as ex:
            conexion.rollback()
            logger.error(f'Error al insertar persona: {ex}')
            
        finally:
            Conexion.cerrar()

    @classmethod
    def eliminar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            valores = (persona.get_id_persona(),)
            cursor.execute(cls.__ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            conexion.rollback()
            logger.error(f'Excepción al eliminar persona:{e}') 
        finally:
            Conexion.cerrar()
            
    @classmethod
    def actualizar(cls, persona):
        try:
            conexion = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_e_mail(), persona.get_id_persona())
            cursor.execute(cls.__ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as ex:
            conexion.rollback()
            logger.error(f'Excepción al actualizar persona: {ex}')
        finally:
            Conexion.cerrar()
    
if __name__ == '__main__':
    """personas = PersonaDao.seleccionar()
    for persona in personas:
        logger.debug(persona)
        logger.debug(persona.get_id_persona())"""
    
    '''
    #Para insertar un nuevo registro
    persona = Persona(nombre='Pedro', apellido='NaJera', e_mail='pnajera@mail.com')
    personas_insertadas = PersonaDao.insertar(persona)
    logger.debug(f'Personas insertadas: {personas_insertadas}')
    '''
    '''
    persona = Persona(id_persona=9)
    personas_eliminadas = PersonaDao.eliminar(persona)
    logger.debug(f'Personas eliminadas: {personas_eliminadas}')
    '''
    persona = Persona(id_persona=23, nombre='Aqui', apellido='Funciona', e_mail='cambiado@mail.com')
    personas_actualizadas = PersonaDao.actualizar(persona)
    logger.debug(f'Personas actualizadas: {personas_actualizadas}')