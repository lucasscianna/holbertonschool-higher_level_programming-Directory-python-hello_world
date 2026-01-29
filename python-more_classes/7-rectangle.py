#!/usr/bin/python3
"""
Définit une classe Rectangle.
"""


class Rectangle:
    """
    Classe qui définit un rectangle.
    """

    # Attribut de classe : nombre d'instances de Rectangle
    number_of_instances = 0

    # Attribut de classe : symbole utilisé pour l'affichage
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise une nouvelle instance de Rectangle.

        Args:
            width (int): largeur du rectangle
            height (int): hauteur du rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Récupère la largeur du rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Définit la largeur du rectangle.

        Raises:
            TypeError: si width n'est pas un entier
            ValueError: si width est inférieur à 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Récupère la hauteur du rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Définit la hauteur du rectangle.

        Raises:
            TypeError: si height n'est pas un entier
            ValueError: si height est inférieur à 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Retourne l'aire du rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Retourne le périmètre du rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Retourne une représentation du rectangle avec print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        lignes = []
        symbole = str(self.print_symbol)

        for _ in range(self.__height):
            lignes.append(symbole * self.__width)

        return "\n".join(lignes)

    def __repr__(self):
        """
        Retourne une chaîne permettant de recréer l'objet avec eval().
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Détecte la suppression d'une instance de Rectangle.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
