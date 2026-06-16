import unittest
from packages.utils import get_logger


class TestRuntime(unittest.TestCase):
    def test_logging(self):
        logger = get_logger(__name__)
        logger.info('Test log message')