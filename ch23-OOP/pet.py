#!/usr/bin/env python3
"""
Chapter 23 - Object Oriented Programming (OOP)
@author Ellery Penas
@version 2018.05.09
"""


class Pet:

    allowed = ['dog', 'cat', 'fish', 'rat']

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You are not allowed to have a {species} pet!")
        self.name = name
        self.species = species

    def set_species(self, species):
        if species not in Pet.allowed:
            raise ValueError(f"You are not allowed to have a {species} pet!")
        self.species = species


def main():
    """main line function"""
    dog = Pet("Spot", "dog")


if __name__ == "__main__":
    main()
