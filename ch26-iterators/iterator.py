#!/usr/bin/env python3
"""
Chapter 26 - Iterators and Operators: writing our own for loop
@author Ellery Penas
@version 2018.05.11
"""


def my_for(object, func):
    iterator = iter(object)
    while True:
        try:
            it = next(iterator)
        except StopIteration:
            break
        else:
            func(it)


def square(x):
    print(x * x)


def main():
    """main line function"""
    my_for("lol", print)
    my_for([1, 2, 3, 4, 5], square)


if __name__ == "__main__":
    main()
