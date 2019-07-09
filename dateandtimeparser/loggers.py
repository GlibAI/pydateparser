"""Singleton logger for all modules to use."""
import logging

formatter = logging.Formatter(
    'DATETIME: %(asctime)s %(levelname)s %(message)s')
file_handler = logging.FileHandler('datetimeparser.log')
file_handler.setFormatter(formatter)
stdout_handler = logging.StreamHandler()
stdout_handler.setFormatter(formatter)

logger = logging.Logger('datetimeparser', level=logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(stdout_handler)
