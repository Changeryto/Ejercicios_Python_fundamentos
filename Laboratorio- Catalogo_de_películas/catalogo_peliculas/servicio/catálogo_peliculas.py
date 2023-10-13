import os

class CatalogoPeliculas:

    ruta = "catalogo.txt"
    @staticmethod
    def agregar_pelicula(Titulo):
        try:
            archivo_peliculas = open(CatalogoPeliculas.ruta, "a") #No olvides que el archivo es una variable estática
            archivo_peliculas.write(str(Titulo) + "\n") #Str debe ser explicito aquí
        except Exception as ex:
            print("\nOcurrió un error en agregar", print(type(ex)), "\n")
        else:
            print("\nTítulo añadido correctamente\n")
        finally:
            archivo_peliculas.close()

    @staticmethod
    def listar_peliculas():
        try:
            archivo_peliculas = open(CatalogoPeliculas.ruta, "r")
            print("\nPeliculas:\n", archivo_peliculas.read(), "\n")
        except Exception as ex:
            print("\nOcurrió un error en listar, verifique que haya agregado películas", print(type(ex)), "\n")
        else:
            print("\nLista desplegada correctamente\n")
        finally:
            archivo_peliculas.close()
            
    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta)
        except Exception as ex:
            print("El archivo ya ha sido eliminado u ocurrió otro problema", type(ex))
        else:
            print("Archivo eliminado con éxito")
        
