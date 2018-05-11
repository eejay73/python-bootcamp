#!/usr/bin/env python3
"""
Chapter 25 - Inheritance: Exploring properties (@property decorator)
@author Ellery Penas
@version 2018.05.11
"""


class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self._age = max(age, 0)

    # exposes the age proerty setters and getters interface
    # users need only to access the prop without the

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = max(age, 0)

    @property
    def full_name(self):
        return f"{self.first} {self.last}"


def main():
    """main line function"""
    john = Human("John", "Doe", 24)
    print(john.age)
    print(john.full_name)

if __name__ == "__main__":
    main()
