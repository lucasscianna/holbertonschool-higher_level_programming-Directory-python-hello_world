#!/usr/bin/python3
"""
Définit une classe Rectangle avec comparaison de rectangles.
"""


class Rectangle:
    """
    Classe qui définit un rectangle.
    """

    # Nombre d'instances de Rectangle
    number_of_instances = 0

    # Symbole utilisé pour l'affichage
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise une instance de Rectangle.

        Args:
            width (int): largeur
            height (int): hauteur
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retourne la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Définit la largeur.

        Raises:
            TypeError: si width n'est pas un entier
            ValueError: si width < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retourne la hauteur."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Définit la hauteur.

        Raises:
            TypeError: si height n'est pas un entier
            ValueError: si height < 0
        """
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
        Retourne le rectangle sous forme de chaîne avec print_symbol.
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
        Détecte la suppression d'une instance.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare deux rectangles et retourne le plus grand (aire).

        Args:
            rect_1 (Rectangle): premier rectangle
            rect_2 (Rectangle): second rectangle

        Raises:
            TypeError: si rect_1 ou rect_2 n'est pas une instance de Rectangle

        Returns:
            Rectangle: le plus grand rectangle (rect_1 si égalité)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
