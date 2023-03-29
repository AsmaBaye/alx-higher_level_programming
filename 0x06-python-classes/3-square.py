#!/usr/bin/python3
"""Module 3-square
This Module contain a defination for a square class
"""


class Square:
    """ A class to define a square objects"""

    def __init__(self, size=0):
        """ A method to intantiate the object of the class with size

        Args:
        size (int, optional): A non negative size is expected . Defaults to 0.
        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
 
    def area(self):
        """A method to return area

        Returns:
            int: area of a square
        """
        return self.__size * self.__size
