#
# Logger exception
#

import logging

logger = logging.getLogger(__name__)

try:
    print(4/2)
    print(2/0)
except ZeroDivisionError:
    logger.error('Here was exception', exc_info = True)