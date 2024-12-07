import logging

from module_2 import devide_number
from module_3 import square_number

logger = logging.getLogger(__name__)

def main():
    a, b = 12, 2
    c, d = 4, 0

    logger.debug('Log DEBUG')
    logger.info('Log INFO')
    logger.warning('Log WARNING')
    logger.error('Log ERROR')
    logger.critical('Log CRITICAL')

    print(devide_number(a, square_number(b)))
    print(devide_number(square_number(c), d))