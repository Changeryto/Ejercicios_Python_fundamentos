class DispositivoEntrada:
    def __init__(self, tipo_entrada, marca):
        self._tipo_entrada = tipo_entrada
        self._marca = marca
    
    #get/set tipo_entrada
    def get_tipo_entrada(self):
        return self._tipo_entrada
    def set_tipo_entrada(self, nuevoTE):
        self._tipo_entrada = nuevoTE
        
    #get/set marca
    def get_marca(self):
        return self._marca
    def set_marca(self, nuevaM):
        self._marca = nuevaM
        
    def __str__(self):
        return "Tipo de entrada: " + self._tipo_entrada + "  Marca: " + self._marca
        
        
"""DE1 = DispositivoEntrada("USB", "HP")
print(DE1)""" #Funciona