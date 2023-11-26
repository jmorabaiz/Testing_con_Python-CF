import logging

# DEBUG = 10 = debug
# INFO = 20 = info
# WARNING = 30 = watning
# ERROR = 40 = error
# CRITICAL = 50 = critical

# Cambiar compartamiento por default
logging.basicConfig(level=logging.DEBUG,
                    format="%(processName)s - %(threadName)s - %(levelname)s - %(asctime)s - Message: %(message)s",
                    datefmt="%Y/%m/%d",
                    filename="codigofacilito.log",
                    filemode="a")


def suma_numeros_positvos(n1: int, n2: int) -> int:
    """
    Permite sumar dos números enteros positivos.
    Args:
        n1: int
        n2: int
    Returns:
        int
    """

    logging.debug('Entramos aquí!!!!')
    # if n1 < 0 or n2 < 0:
    #     return None
    assert n1 > 0 and n2 > 0, 'Lo sentimos solo es posible sumar nros positivos'
    logging.debug('Nos encontramos en esta línea.')

    return n1 + n2


if __name__ == '__main__':
    logging.debug('Antes del llamado de la función.')

    resultado = suma_numeros_positvos(10, 20)
    logging.info(resultado)
