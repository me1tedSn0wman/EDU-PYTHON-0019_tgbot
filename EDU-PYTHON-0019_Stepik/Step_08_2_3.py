import logging
import sys


logger = logging.getLogger(__name__)

stderr_handler = logging.StreamHandler()
stdout_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)

print(logger.handlers)

logger.warning('This is log with wornings')