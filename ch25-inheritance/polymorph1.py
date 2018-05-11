#!/usr/bin/env python3
"""
Chapter 25 - Inheritance: exploring polymorphisum
            - when a single class method works similar in different classes
@author Ellery Penas
@version 2018.05.11
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError(
            "Subclass needs to implement the speak method")


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        return "woof"


class Fish(Animal):
    pass


def main():
    """main line function"""
    d = Dog("Spot")
    print(d.speak())
    f = Fish("Nemo")
    print(f.speak())  # NotImplementedError


if __name__ == "__main__":
    main()
