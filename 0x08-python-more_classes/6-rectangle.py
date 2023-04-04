#!/usr/bin/python3
'''
Module contains Rectangle Class
'''


class Rectangle:
    '''An empty rectangle class
    '''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''Initialises the Rectangle class
        args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        '''Returns the width property'''
        return self.__width

    @width.setter\n    def width(self, value):
        '''The setter of the width peoperty
        args:
            value (int): The value of the width property
        '''
        self.validate_input('width', value)
        self.__width = value

    @property
    def height(self):
        '''Returns the height property'''
        return self.__height

    @height.setter
    def height(self, value):
        '''The setter of the height peoperty
        args:
            value (int): The value of the height property
        '''
        self.validate_input('height', value)
        self.__height = value

    def area(self):
        '''Returns the area of the rectangle
        Returns:
            The area
        '''
        return self.__width * self.__height

    def perimeter(self):
        '''Returns the  perimeter of the rectangle
        Returns:
            The perimeter
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''Prints the rectangle using char #'''
        shape = ''
        if self.__width == 0 or self.__height == 0:
            return shape

        for i in range(self.__height):
            for j in range(self.__width):
                shape += '#'
            if i != self.__height - 1:
                shape += '\n'

        return shape

    def __repr__(self):
        '''
        Returns string representation of the Rectangle
        '''
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        '''
        Prints a message when an instance of an object is about to be destroyed
        '''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def validate_input(self, property_name: str, value: int):
        if not isinstance(value, int):
            raise TypeError(f"{property_name} must be an integer")
        elif value < 0:
            raise ValueError(f"{property_name} must be >= 0")
