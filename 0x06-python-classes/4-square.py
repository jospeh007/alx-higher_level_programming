#!/usr/bin/python3
"""Square module."""


class Square:
    """Defines an empty square."""

    def __init__(self, size=0):
        """More important.

        Args:
            size: Length of a size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Property for the length of the size square.

        Exception:
            TypeError: If the size is not an int
            ValueError: If the size is less than 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """The area of the square.

        Returns:
            The size of the square area.
        """
        return self.__size ** 2
