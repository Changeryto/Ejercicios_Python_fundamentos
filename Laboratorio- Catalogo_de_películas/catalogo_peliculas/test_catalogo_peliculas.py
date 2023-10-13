#Catálogo de películas
from dominio.pelicula import Pelicula
from servicio.catálogo_peliculas import CatalogoPeliculas
x = None
print("Catálogo de películas\n\n")
while x != "4":
    try:
        x = input("¿Qué desea hacer? (introduzca el número): \n1: Agregar película \n2: Listar películas \n3: Borrar películas guardadas \n4: Salir \n\n Acción:  ")
        if x == "1":
            pelicula_nueva = input("\nIntrocuce el nombre de la película: ")
            nueva_pelicula = Pelicula(pelicula_nueva)
            CatalogoPeliculas.agregar_pelicula(nueva_pelicula)
        elif x == "2":
            CatalogoPeliculas.listar_peliculas()
        elif x == "3":
            CatalogoPeliculas.eliminar()
        elif x == "4":
            print("\nAdios UwU\n")
        elif x == "no" or x == "No" or x == "NO" or x == "nO":
            print("\nPues me voy >:v\n")
            break
        else:
            print("\nPor favor introduce una acción válida\n")
    except Exception as ex:
        print("Ocurrió un problema en el test", type(ex))
    