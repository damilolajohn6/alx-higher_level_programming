#!/usr/bin/python3
'''
Module contains Rectangle Class
'''

class Rectangle:
    """A class defining a rectangle."""
    
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance.
        
        Parameters
        ----------
        width : int
            Width of the rectangle. Defaults to 0.
        height : int
            Height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """Getter for width attribute."""
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Setter for width attribute.
        
        Parameters
        ----------
        value : int
            The new value for the width attribute.
        
        Raises
        ------
        TypeError
            If value is not an integer.
        ValueError
            If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer.")
        elif value < 0:
            raise ValueError("Width must not be negative.")
        else:
            self.__width = value
    
    @property
    def height(self):
        """Getter for height attribute."""
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Setter for height attribute.
        
        Parameters
        ----------
        value : int
            The new value for the height attribute.
        
        Raises
        ------
        TypeError
            If value is not an integer.
        ValueError
            If value is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer.")
        elif value < 0:
            raise ValueError("Height must not be negative.")
        else:
            self.__height = value
    
    def area(self):
        """
        Calculates the area of the rectangle.
        
        Returns
        -------
        int
            The area of the rectangle.
        """
        return self.__width * self.__height
    
    def perimeter(self):
        """
        Calculates the perimeter of the rectangle.
        
        Returns
        -------
        int
            The perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """
        Returns a graphical representation of the rectangle.
        
        Returns
        -------
        str
            A newline-separated string of '#' characters representing the rectangle.
        """
        return '\n'.join(['#' * self.__width] * self.__height)
