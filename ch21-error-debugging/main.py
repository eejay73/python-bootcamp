#!/usr/bin/env python3
"""
CH21 - Errors and Debugging
@author Ellery Penas
@version 2018.04.18
"""


def colorize(text, color):
    colors = ('red', 'green', 'blue')
    if not isinstance(text, str):
        raise TypeError("Type of text must be an instance of str")
    if color not in colors:
        raise TypeError(
            f"Invalid color specified '{color}': valid colors are red, green or blue")
    print(f"printed {text} in the color {color}")


def get(d, key):
    """
    Will catch KeyError exception if key does not exist on dict
    """
    try:
        return d[key]
    except KeyError:
        return None


def main():
    """main line function"""
    # raise ValueError("blah blah")
    # colorize("Hello", "red")
    # colorize("Hello", "yellow")
    # colorize(10, "red")  # will raise TypeError

    # try - except exploration
    d = {"name": "Jeff"}
    print(get(d, "name"))
    print(get(d, "city"))  # raises KeyError as city does not exist


if __name__ == "__main__":
    main()
