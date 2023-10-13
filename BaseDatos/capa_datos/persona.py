from logger_base import logger

class Persona:
    #ASí creamos in valor por default
    def __init__(self, id_persona=None, nombre=None, apellido=None, e_mail=None):
        self.__id_persona = id_persona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__e_mail = e_mail
        
    def __str__(self):
        return (
            f'Id Persona: {self.__id_persona}, '
            f'Nombre: {self.__nombre}, '
            f'Apellido: {self.__apellido}, '
            f'Email: {self.__e_mail}'
        )
        
    def get_id_persona(self):
        return self.__id_persona
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_e_mail(self):
        return self.__e_mail
    
    def set_id_persona(self, id_persona):
        self.__id_persona = id_persona
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_apellido(self, apellido):
        self.__apellido = apellido
    def set_e_mail(self, e_mail):
        self.__e_mail = e_mail
        
        
if __name__ == '__main__':
    persona1 = Persona(1, 'Juan', 'Perez', 'email_genérico')
    logger.debug(persona1)
    #Simulando un objeto a insertar de tipo persona
    
    
    #Lo mejor para no proporcionar informacion no deseada
    persona2 = Persona(nombre='Karla', apellido='Gomez', e_mail='kgomez@mail.com')
    logger.debug(persona2)
    
    #Simular el caso de eliminar un objeto de tipo persona
    persona3 = Persona(id_persona=3)
    logger.debug(persona3)