from logger_base import logger


class Usuario:
    def __init__(self, id_usuario=None, username=None, password=None):
        self.__id_usuario = id_usuario
        self.__username = username
        self.__password = password
        
    def __str__(self):
        return(
            f'ID Usuario: {self.__id_usuario}, '
            f'Username: {self.__username}, '
            f'Password: {self.__password}'
        )
        
    def get_id_usuario(self):
        return self.__id_usuario
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def set_id_usuario(self, nuevo_id_usuario):
        self.__id_usuario = nuevo_id_usuario
        
    def set_username(self, nuevo_username):
        self.__username = nuevo_username
        
    def set_password(self, nueva_password):
        self.__password = nueva_password
        
        
if __name__ == '__main__':
    usuario1 = Usuario(1, 'Changery', 'Bonito')
    logger.info(usuario1)