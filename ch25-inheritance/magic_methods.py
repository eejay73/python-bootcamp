#!/usr/bin/env python3
"""
Chapter 25 - Inheritance: exploring polymorphisum
            - explore overriding magic methods of standard objects
@author Ellery Penas
@version 2018.05.11
"""


class GrumpyDict(dict):
    def __repr__(self):
        print('NONE OF YOUR BUSINESS!!!!')
        return super().__repr__()

    def __missing__(self, key):
        print(f'YOU WANT {key}? WELL IT AINT HERE!')

    def __setitem__(self, key, value):
        print('AAHHHHH..FINE! WHATEVER!')
        return super().__setitem(key, value)


def main():
    """main line function"""
    data = GrumpyDict({
        "name": "John",
        "city": "SF"
    })

    print(data)
    print(data['pet'])
    print(data['city'])

if __name__ == "__main__":
    main()
