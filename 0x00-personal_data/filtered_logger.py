#!/usr/bin/env python3
"""
logging tasks

"""
from typing import List
import re
import logging


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
