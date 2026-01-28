#!/usr/bin/python3
"""
Module Square
Définit une classe Square avec :
- taille privée
- getter et setter avec validation
- calcul de l'aire
- affichage du carré avec #
"""

class Square:
    """
    Classe Square qui définit un carré avec :
    - un attribut privé __size
    - validation de type et valeur
    - méthodes area() et my_print()
    """

    def __init__(self, size=0):
        """
        Constructeur d'un carré.

        Args:
            size (int): Taille du côté du carré (par défaut 0).

        Utilise le setter pour initialiser la taille afin de valider type et valeur.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter de la taille du carré.

        Returns:
            int: valeur actuelle de la taille du carré.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter de la taille du carré avec validation.

        Args:
            value (int): nouvelle taille à assigner.

        Raises:
            TypeError: si value n'est pas un entier.
            ValueError: si value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Stocke la valeur validée dans l'attribut privé

    def area(self):
        """
        Calcule l'aire du carré.

        Returns:
            int: aire du carré (size * size).
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Affiche le carré avec le caractère # sur stdout.

        Si la taille est 0, affiche une ligne vide"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print('#' * self.__size)

