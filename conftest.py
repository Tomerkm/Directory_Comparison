import configparser
import sys

import pytest
from definitions import CONFIG_FILE_NAME
import logging

mapping_logging_level = \
    {
        "NOTSET": logging.NOTSET,
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }


@pytest.fixture(scope="function")
def get_config():
    config_obj = configparser.ConfigParser()
    config_obj.read(CONFIG_FILE_NAME)

    return config_obj


@pytest.fixture(scope="function")
def get_test_name(request):
    return request.node.name


@pytest.fixture(scope="function")
def get_logger(get_test_name, get_config):
    logger = logging.getLogger(name=get_test_name)

    log_level = mapping_logging_level[get_config["LOG_CONFIG"]["level"].upper().replace(" ", "")]
    formatter = get_config["LOG_CONFIG"]["formatter"].lower()
    date_formatter = get_config["LOG_CONFIG"]["date_formatter"]

    # Set the threshold logging level of the logger to INFO
    logger.setLevel(level=log_level)
    # Create a stream-based handler that writes the log entries
    # into the standard output stream
    handler = logging.StreamHandler(stream=sys.stdout)
    # Create a formatter for the logs
    formatter = logging.Formatter(fmt=formatter, datefmt=date_formatter)
    # Set the created formatter as the formatter of the handler
    handler.setFormatter(fmt=formatter)
    # Add the created handler to this logger
    logger.addHandler(hdlr=handler)

    return logger
