#!/usr/bin/env python3
"""
Chapter 26 - Iterators and Operators
@author Ellery Penas
@version 2018.05.11
"""
# override the __iter__ and __next__ dunders to create a custom iterable


class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


def main():
    """main line function"""
    for num in Counter(0, 10):
        print(num)


if __name__ == "__main__":
    main()
