#!/usr/bin/python3
"""Module: 2-append_write
This is a function that appends a string at the end of a text file (UTF8)
Returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends the given text to the end of the file with the given filename (or creates it if it doesn't exist).
    Returns the number of characters added to the file.
    """
    
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
