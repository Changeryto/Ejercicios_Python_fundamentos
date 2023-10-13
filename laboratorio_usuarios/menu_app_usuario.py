#! python3
from usuario import Usuario
from usuarioDAO import UsuarioDao
from usuarioDAO import UsuarioDao
from logger_base import logger

a = 0
#Inicio del menú
while a == 0:
    try:
        acto = input('\nOpciones:\n1. Listar usuarios\n2. Agregar usuarion\n3. Modificar usuario\n4. Eliminar usuario\n5. Salir\n\nEscribe tu opción + [Enter] (1-5):  ')
        if acto == '1':
            usuarios = UsuarioDao.seleccionar()
            for usuario in usuarios:
                logger.info(usuario)
                
        elif acto == '2':
            
            try:
                n_username = input('Nuevo username: ')
                n_password = input('Nuevo password: ')
                n_usuario = Usuario(username=n_username, password=n_password)
                usuarios_insertados = UsuarioDao.insertar(n_usuario)
                logger.info(f'Usuarios insertados: {usuarios_insertados}')
            except Exception as ex:
                logger.error(f'Hubo una excepción en el acto 2: {ex}, {type(ex)}')
                
        elif acto == '3':
            
            try:
                id_usuario = input('Introduzca el ID del usuario a modificar: ')
                n_username = input('Introduzca el nuevo username: ')
                n_password = input('Introduzca el nuevo password: ')
                a_usuario = Usuario(id_usuario=id_usuario, username=n_username, password=n_password)
                usuarios_actualizados = UsuarioDao.actualizar(a_usuario)
                logger.info(f'Usuarios actualizados: {usuarios_actualizados}')
            except Exception as ex:
                logger.error(f'Hubo una excepción al actualizar {ex, type(ex)}')
                
        elif acto == '4':
            
            try:
                id_usuario = input('Introduzca el ID del usuario a eliminar: ')
                e_usuario = Usuario(id_usuario=id_usuario)
                usuarios_eliminados = UsuarioDao.eliminar(e_usuario)
                logger.info(f'Usuarios eliminados: {usuarios_eliminados}')
            except Exception as ex:
                logger.error(f'Verifica que el ID exista, no se puede eliminar un usuario de ID inexistente: {ex, type(ex)}')
                
        elif acto == '5':
            
            break
        
        else:
            logger.info(f'Por favor introduzca sólo opciones existentes nwn')
                
    except Exception as ex:
        print('Por favor inserta sólo opciones válidas: ', ex, type(ex))
