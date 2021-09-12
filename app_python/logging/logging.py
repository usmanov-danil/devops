import logging
from typing import NewType

from loguru import logger

LoguruHandler = NewType('LoguruHandler', dict[str, any])


class InterceptHandler(logging.Handler):
    """
    Default handler from examples in loguru documentation.
    https://loguru.readthedocs.io/en/stable/overview.html#entirely-compatible-with-standard-logging
    """

    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage()
        )

def setup_logger():
    logging.getLogger().handlers = [InterceptHandler()]
    logger.add('/tmp/logs/app_python.log', level='INFO', rotation='1 day')