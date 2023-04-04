#!/usr/bin/python3
"""
This module is composed by a class that defines a Rectangle
"""


class Rectangle:
    """ Class that defines a rectangle """
number_of_instances = 0
print_symbol = "#"

def __init__(self, width=0, height=0):
    """Initialize the instance.
    
    Args:
        width (int): Rectangle width.
        height (int): Rectangle height.
    """

    self._width = width
    self._height = height
    Rectangle.number_of_instances += 1

@property
def width(self):
    """Return the value of the width."""

    return self._width

@width.setter
def width(self, value):
    """Set the value of the width.
    
    Args:
        value (int): Rectangle width.
        
    Raises:
        TypeError: If width is not an integer.
        ValueError: If width is less than zero.
    """

    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self._width = value

@property
def height(self):
    """Return the value of the height."""

    return self._height

@height.setter
def height(self, value):
    """Set the value of the height.
    
    Args:
        value (int): Rectangle height.
        
    Raises:
        TypeError: If height is not an integer.
        ValueError: If height is less than zero.
    """

    if not isinstance(value, int):
        raise TypeError("height must be an integer")
    if value < 0:
        raise ValueError("height must be >= 0")
    self._height = value

def area(self):
    """Return the area of the rectangle."""

    return self.width * self.height

def perimeter(self):
    """Return the perimeter of the rectangle."""

    if self.width == 0 or self.height == 0:
        return 0

    return (2 * self.width) + (2 * self.height)

def __str__(self):
    """Return a string representation of the rectangle."""

    if self.width == 0 or self.height == 0:
        return ""
    
    return ((str(self.print_symbol) * self.width + "\n") * self.height).rstrip()

def __repr__(self):
    """Return a string representation of the instance."""

    return f"Rectangle({self.width}, {self.height})"

def __del__(self):
    """Print a message when the instance is deleted."""

    Rectangle.number_of_instances -= 1
    print("Bye rectangle...") 
