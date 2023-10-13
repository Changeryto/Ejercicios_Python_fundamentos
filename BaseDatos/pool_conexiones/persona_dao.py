from persona import Persona
from cursor_del_pool import CursorDelPool
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
        '''El bloque with llama los métodos de forma automática __enter__ --> __exit__'''
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECCIONAR)) #Imprime el logging en la BD
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_e_mail())
            cursor.execute(cls.__INSERTAR, valores)
            return cursor.rowcount ################ Sin Paréntesis es variable, no método


    @classmethod
    def eliminar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            valores = (persona.get_id_persona(),)
            cursor.execute(cls.__ELIMINAR, valores)
            return cursor.rowcount

            
    @classmethod
    def actualizar(cls, persona):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_e_mail(), persona.get_id_persona())
            cursor.execute(cls.__ACTUALIZAR, valores)
            return cursor.rowcount
    
if __name__ == '__main__':
    
    personas = PersonaDao.seleccionar()
    for persona in personas:
        logger.debug(persona)
    
    
    """
    #Para insertar un nuevo registro
    persona = Persona(nombre='Pedro2', apellido='NaJera2', e_mail='pnajera@mail.com2')
    personas_insertadas = PersonaDao.insertar(persona)
    logger.debug(f'Personas insertadas: {personas_insertadas}')
    """
    '''
    persona = Persona(id_persona=23)
    personas_eliminadas = PersonaDao.eliminar(persona)
    logger.debug(f'Personas eliminadas: {personas_eliminadas}')
    ''' 
    """
    persona = Persona(id_persona=23, nombre='Juan', apellido='Parza', e_mail='chimewe@mail.com')
    personas_actualizadas = PersonaDao.actualizar(persona)
    logger.debug(f'Personas actualizadas: {personas_actualizadas}')
    """