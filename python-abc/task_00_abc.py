#!/usr/bin/python3
"""Abstract Base Class Animal"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract animal with sound method"""

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """Dog barking sound"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat meowing sound"""
    def sound(self):
        return "Meow"
