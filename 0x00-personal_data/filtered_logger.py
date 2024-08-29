#!/usr/bin/env python3
"""
This module provides a function to obfuscate specific fields in log messages.
"""

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields (List[str]): The list of fields to be obfuscated.
        redaction (str): The string used to replace the field values.
        message (str): The log message to be filtered.
        separator (str): The character used to separate the fields in the log message.

    Returns:
        str: The obfuscated log message.
    """
    pattern = f"({'|'.join(fields)})=([^ {separator}]+)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)
