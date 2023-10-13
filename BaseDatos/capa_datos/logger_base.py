import logging
# DEBUG, INFO, WARNING, ERROR, CRITICAL

"""Variable logger a utilizar"""
logger = logging

logger.basicConfig(level=logging.DEBUG,
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                   datefmt='%I:%M:%S %p',
                   handlers=[logging.FileHandler('capa_datos.log'),  # Manda la información al archivo
                             logging.StreamHandler()])  # Especifica a qué nivel se manda información a la consola
# Por defecto a niver WARNING, DEBUG se utiliza al depurar programas
# Así obligamos a que los siguientes comandos no se ejecuten en otros archivos.
if __name__ == '__main__':
    logging.warning("Mensaje a nivel warning")
    logging.info("Mensaje a nivel info")
    logging.debug("Mensaje a nivel debug")

    # Por ejemplo si tenemos un error en la BD
    logging.error("Ocurrió un error en la base de datos")

    # Por ejemplo si sólo obtenemos un mensaje de conexión
    logging.debug("Se realizó la conexión con éxito")
