#!/usr/bin/python3
"""
5-text_indentation module
This module contains a function that prints a text with 2 new lines
after each '.', '?' or ':'
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' or ':'

    Args:
        text (str): text to print

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        buffer += char
        if char in ".?:":
            print(buffer.strip())
            print()
            buffer = ""
    if buffer:
        print(buffer.strip())
