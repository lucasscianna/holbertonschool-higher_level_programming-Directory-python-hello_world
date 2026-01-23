#!/usr/bin/python3
"""Prints a text with 2 new lines after each of these characters: ., ? and:
"""


def text_indentation(text):
    """Prints a text with 2 new lines after each . ? :

    Args:
        text (str): The input text

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    if len(text) == 0:
        return

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            # Saute les espaces qui suivent le caractère spécial
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
