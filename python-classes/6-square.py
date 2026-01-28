#!/usr/bin/python3
"""
Module Square
Définit une classe Square avec :
- taille privée
- position privée
- getter et setter avec validation
- calcul de l'aire
- affichage du carré avec # respectant la position
"""

class Square:
    """
    Classe Square qui définit un carré avec :
    - un attribut privé __size
    - un attribut privé __position
    - validation de type et valeur
    - méthodes area() et my_print()
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Constructeur d'un carré.

        Args:
            size (int): taille du côté du carré (par défaut 0)
            position (tuple): position du carré (par défaut (0, 0))

        Utilise les setters pour valider et stocker size et position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter pour la taille du carré.

        Returns:
            int: taille actuelle du carré
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter pour modifier la taille du carré avec validation.

        Args:
            value (int): nouvelle taille

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Getter pour la position du carré.

        Returns:
            tuple: position actuelle du carré (x, y)
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter pour modifier la position du carré avec validation.

        Args:
            value (tuple): nouvelle position (x, y)

        Raises:
            TypeError: si value n'est pas un tuple de 2 entiers >= 0
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) and num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: aire du carré
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Affiche le carré avec le caractère # sur stdout."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
