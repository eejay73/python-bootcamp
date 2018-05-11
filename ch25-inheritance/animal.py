#!/usr/bin/env python3
"""
Chapter 25 - Inheritance
@author Ellery Penas
@version 2018.05.11
"""


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"

    def make_sound(self, sound):
        return f"{self.name} goes {sound}"


class Dog(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Dog")
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


def main():
    """main line function"""
    dog = Dog("Spot", "Boxer", "Bone")
    print(dog)
    dog.play()


if __name__ == "__main__":
    main()
