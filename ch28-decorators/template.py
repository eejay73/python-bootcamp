#!/usr/bin/env python3
"""
Chapter 28 - Decorators
@author Ellery Penas
@version 2018.05.11
"""


def be_polite(fn):

    def wrapper():
        print("Pressure to meet you.")
        fn()
        print("Have a wonderful day.")

    return wrapper


def greet():
    print("My name is John.")


def main():
    """main line function"""

    wrapped_greet = be_polite(greet)
    wrapped_greet()


if __name__ == "__main__":
    main()
