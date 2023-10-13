from usuario import Usuario
from cursor_del_pool import CursorDelPool
from logger_base import logger


class UsuarioDao:
    __INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    __SELECCIONAR = 'SELECT * FROM usuario ORDER BY id_usuario' #'SELECT * FROM persona ORDER BY id_persona'
    __ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario = %s'
    __ELIMINAR = 'DELETE FROM usuario WHERE id_usuario = %s'
    
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
        
    """    
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
            return personas"""
        
        
    @classmethod
    def insertar(cls, usuario):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.get_username(), usuario.get_password())
            cursor.execute(cls.__INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, usuario):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.get_username(), usuario.get_password(), usuario.get_id_usuario())
            cursor.execute(cls.__ACTUALIZAR, valores)
            return cursor.rowcount
        
    @classmethod
    def eliminar(cls, usuario):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Usuario a eliminar: {usuario}')
            valores = (usuario.get_id_usuario(),)
            cursor.execute(cls.__ELIMINAR, valores)
            return cursor.rowcount
            
            
if __name__ == '__main__':
    
    
    usuarios = UsuarioDao.seleccionar()
    for usuario in usuarios:
        logger.info(usuario)
    
    '''
    usuario = Usuario(username='Changery', password='zapatos')
    usuarios_insertados = UsuarioDao.insertar(usuario)
    logger.info(f'Usuarios insertados: {usuarios_insertados}')'''