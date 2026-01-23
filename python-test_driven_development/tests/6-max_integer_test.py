#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Classe de test pour la fonction max_integer"""

    def test_ordered_list(self):
        """Teste une liste ordonnée"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Teste une liste non ordonnée"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Teste une liste avec le max au début"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Teste une liste vide"""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Teste une liste avec un seul élément"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Teste une liste avec des nombres flottants"""
        self.assertEqual(max_integer([1.53, 6.33, -9.12, 14.1, 6.0]), 14.1)

    def test_ints_and_floats(self):
        """Teste une liste mélangeant entiers et flottants"""
        self.assertEqual(max_integer([1.53, 15.5, 10, 15, 6.0]), 15.5)

    def test_string(self):
        """Teste une chaîne de caractères (doit retourner le caractère max)"""
        self.assertEqual(max_integer("Holberton"), 't')

    def test_list_of_strings(self):
        """Teste une liste de chaînes de caractères"""
        self.assertEqual(max_integer(["abc", "xyz"]), "xyz")

    def test_none_argument(self):
        """Teste le passage de None (doit lever une TypeError)"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_negative_numbers(self):
        """Teste une liste avec uniquement des nombres négatifs"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

if __name__ == '__main__':
    unittest.main()
