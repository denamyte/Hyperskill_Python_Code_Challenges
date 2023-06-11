# import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
log_format = "%(levelname)s -> %(message)s"
handler.setFormatter(logging.Formatter(log_format))
logger.addHandler(handler)


def hypotenuse(a, b):
    h = round(((a ** 2 + b ** 2) ** 0.5), 2) 
    logger.info(f'Hypotenuse of {a} and {b} is {h}')
    return h
