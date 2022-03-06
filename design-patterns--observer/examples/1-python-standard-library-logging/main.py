# Adapted from
# https://docs.python.org/3/howto/logging-cookbook.html#multiple-handlers-and-formatters

import logging
from logging.config import dictConfig

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "all_logs_to_file": {
            "class": "logging.FileHandler",
            "filename": "spam.log",
            "formatter": "standard",
            "level": "DEBUG",
        },
        "error_to_console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "level": "ERROR",
        },
    },
    "loggers": {
        "": {
            "handlers": ["all_logs_to_file", "error_to_console"],
            "level": "DEBUG",
        }
    },
}

# load configuration and set up logger
dictConfig(LOGGING_CONFIG)
logger = logging.getLogger()

# log
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.critical('critical message')
logger.error('error message')
