#!/usr/bin/env python3
"""
logging tasks

"""
from typing import List
import re
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        return filter_datum(
                self.fields,
                self.REDACTION, super().format(record), self.SEPARATOR)


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """
    a function that uses re.sub to replace something in the message
    """
    pattern = r'(' + '|'.join([f'{field}=.*?{separator}' for field in fields]) + ')'
    return re.sub(
            pattern,
            lambda a: f"{a.group().split('=')[0]}={redaction}{separator}",
            message)
