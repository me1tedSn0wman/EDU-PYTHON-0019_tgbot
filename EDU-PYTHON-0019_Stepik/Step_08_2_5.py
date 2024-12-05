import logging

class ErrorLogFilter(logging.Filter):
    def filter(self, record):
        return record.levelname == 'ERROR' and 'важно' in record.msg.lower()
    
logger =logging.getLogger(__name__)

stderr_handler = logging.StreamHandler()
stderr_handler.addFilter(ErrorLogFilter())

logger.addHandler(stderr_handler)

logger.warning('Важно! Лог с предупреждением')
logger.error('Важно! Лог с ошибкой')
logger.info('Важно! Лог с уровня INFO')
logger.error('Лог с ошибкой')

