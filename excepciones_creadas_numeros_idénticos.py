class NumerosIdenticosException(Exception):
    def __init__(self, mensaje):
        self.message = mensaje #El atributo de message está definido dentro de la clase padre
        