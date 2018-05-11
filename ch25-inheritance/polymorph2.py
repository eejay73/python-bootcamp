#!/usr/bin/env python3
"""
Chapter 25 - Inheritance: exploring polymorphisum
            - when a single method can work on different object types
            - working with 'Magic Methods' e.g. __len__, dounders
@author Ellery Penas
@version 2018.05.11
"""
from copy import copy


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} age of {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human("Newborn", self.last, age=0)
        raise TypeError("Can only add 2 Humans together!")

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]
        raise TypeError(
            "Invalid mutlpler; second parameter must be an interger")


def main():
    """main line function"""
    j = Human("Jane", "Doe", 30)
    s = Human("John", "Smith", 31)
    print(len(j))
    print(j + s)

    trips = j * 3
    print(trips[1].first)
    trips[1].first = 'fsadfasdf'
    print(trips)


if __name__ == "__main__":
    main()
