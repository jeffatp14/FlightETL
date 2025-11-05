import logging
import sys

logger = None
def get_handler():
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter("[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s")
    handler.setFormatter(formatter)

    return handler

def get_logger():
    global logger
    if not logger:
        logger = logging.getLogger('__name__')
        logger.setLevel(logging.INFO)
        logger.addHandler(get_handler())
    return logger