#!/usr/bin/python3
"""Module définissant une classe Rectangle avec largeur et hauteur."""

class Rectangle:
    """Classe Rectangle qui définit un rectangle par sa largeur et sa hauteur."""
    number_of_instances = 0
    def __init__(self, width=0, height=0):
        """Initialise un rectangle avec une largeur et une hauteur."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
    @property
    def width(self):
        """Récupère la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Modifie la largeur du rectangle après validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Modifie la hauteur du rectangle après validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l'aire du rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre du rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)


    def __str__(self):
        """
        Return the string representation using #.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle = ""
        for _ in range(self.__height):
            rectangle += "#" * self.__width + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """
        Return a string representation to recreate the instance.
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Print a message when a Rectangle instance is deleted.
        """
        print("Bye rectangle...")