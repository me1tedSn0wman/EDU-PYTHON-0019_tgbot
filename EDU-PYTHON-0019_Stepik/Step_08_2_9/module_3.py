import logging

logger =logging.getLogger(__name__)

def square_number(number: int | float):

    logger.debug('Log DEBUG')
    logger.info('Log INFO')
    logger.warning('Log WARNING')
    logger.error('Log ERROR')
    logger.critical('Log CRITICAL')

    return number**2