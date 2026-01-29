#!/usr/bin/python3
"""
Définit une classe Rectangle avec comparaison, suivi d'instances et création de carré.
"""


class Rectangle:
    """
    Classe qui définit un rectangle avec :
    - largeur et hauteur privées
    - suivi du nombre d'instances
    - symbole d'affichage
    - méthodes pour aire, périmètre, string, repr, comparaison, carré
    """

    # Nombre d'instances
    number_of_instances = 0

    # Symbole pour l'affichage du rectangle
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialise le rectangle.

        Args:
            width (int): largeur
            height (int): hauteur
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # incrémente le compteur

    @property
    def width(self):
        """Retourne la largeur."""
        return self.__width

    @width.setter
    def width(self, value):
        """Définit la largeur avec validation."""
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
        """Définit la hauteur avec validation."""
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
        """Retourne le rectangle sous forme de chaîne avec print_symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbole = str(self.print_symbol)
        lignes = [symbole * self.__width for _ in range(self.__height)]
        return "\n".join(lignes)

    def __repr__(self):
        """Retourne une chaîne pour recréer l'objet avec eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Détecte la suppression d'une instance et décrémente le compteur."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare deux rectangles et retourne le plus grand.

        Args:
            rect_1 (Rectangle)
            rect_2 (Rectangle)

        Returns:
            Rectangle: le rectangle ayant la plus grande aire, rect_1 si égalité

        Raises:
            TypeError: si rect_1 ou rect_2 n'est pas un Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Crée un rectangle dont la largeur = hauteur = size.

        Args:
            size (int): taille du côté du carré

        Returns:
            Rectangle: nouvelle instance carré
        """
        return cls(size, size)
