import sys

from loguru import logger


def configure_logging():

    logger.remove()

    logger.add(
        sys.stdout,
        level="INFO",
        backtrace=True,
        diagnose=True,
        enqueue=True,
        colorize=True,
    )

    return logger