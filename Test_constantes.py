# from Constantes_en_python import * #Permite importar todo, pero se debe usar el nombre orgiginal

from Constantes_en_python import MI_CONSTANTE
from Constantes_en_python import Matematicas as mate

print(MI_CONSTANTE)
print(mate.PI)


MI_CONSTANTE = "Nuevo valor"
mate.PI = 3.14

print(MI_CONSTANTE)
print(mate.PI)