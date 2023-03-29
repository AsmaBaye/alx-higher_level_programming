#!/usr/bin/python3
"""Module 1-square
This module contains a defination of a square class
"""


class Square:
    """A class that represnt a square"""
    def __init__(self, size=0):
        """Intialize a class with size validation
        Args:
        size (int): size of int greater than zero_. Defaults to 0.
        """
        
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size<0:
            raise ValueError("size must be >= 0")          
        self.__size = size
