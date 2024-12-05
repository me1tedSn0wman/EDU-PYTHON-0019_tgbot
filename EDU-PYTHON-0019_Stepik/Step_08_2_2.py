import logging

logger = logging.getLogger()

logging.basicConfig(
    level=logging.DEBUG,
    format = '[{asctime}] #{levelname:8} {filename}:'
             '{lineno} - {name} - {message}',
    style = '{'
)

logger =logging.getLogger(__name__)

logger.debug('Log level DEBUG')