import logging

logger = logging.getLogger(__name__)

def devide_number(dividend: int | float, devider: int | float):

    logger.debug('Log DEBUG')
    logger.info('Log INFO')
    logger.warning('Log WARNING')
    logger.error('Log ERROR')
    logger.critical('Log CRITICAL')

    try:
        return dividend / devider
    except ZeroDivisionError:
        logger.exception('Devide by 0')