import logging
import sys


def init_logger(verbose: bool = True) -> logging.Logger:
    # Init logger instance
    logging.basicConfig(stream=sys.stderr, format="%(levelname)-8s  %(message)s")

    # Assign logger instance a name
    logger: logging.Logger = logging.getLogger(__name__)

    logger.setLevel(logging.INFO)
    if verbose:
        logger.setLevel(logging.DEBUG)

    return logger
