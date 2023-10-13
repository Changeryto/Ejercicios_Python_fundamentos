import logging

logger = logging
logger.basicConfig(level=logging.INFO,
                   format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                   datefmt='%I:%M:%S %p',
                   handlers=[logging.FileHandler('capa_datos.log'),
                             logging.StreamHandler()])

