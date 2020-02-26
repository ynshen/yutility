"""Test code for log module"""

from yutility import logging
from yutility.log import Logger
import pandas as pd
from pytest import raises


def test_Logger_can_log():

    logger = Logger()
    assert isinstance(logger.log, pd.DataFrame)

    logger.info('Some message')
    assert logger.log.iloc[-1]['message'] == 'Some message'


def test_logging_can_log():
    logging.info('Some info')
    logging.warning("Some warning")
    with raises(ValueError):
        logging.error("let's get some ValueError", error_type=ValueError)

