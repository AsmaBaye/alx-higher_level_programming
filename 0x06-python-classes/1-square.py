#!/usr/bin/python3

"""Module 1-square 

This module contain a defination for square class with priv attr
"""
 
 
class Square:
    """A class that define a square"""
    
    def __init__(self,size):
        """Intialize a class with a size
        Args:
        	size: _the size of a square
		"""
        self.__size = size
