import logging

class EvenLogFilter(logging.Filter):
    def filter(self, record):
        return not record.i % 2
    
logger =logging.getLogger(__name__)

stderr_handler = logging.StreamHandler()
stderr_handler.addFilter(EvenLogFilter())

logger.addHandler(stderr_handler)

for i in range(1,5):
    logger.warning('Важно! это лог с предупреждением! %d', i, extra={'i':i})

