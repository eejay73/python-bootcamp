#!/usr/bin/env python3
"""
First codenvy file.
@author Ellery Penas
@version 2018.04.07
"""
from termcolor import colored


def main():
    """main line function"""
    # dir() will print out all the functions within an object
    # print(dir(termcolor))
    # help(termcolor)

    text = colored("hello", "red", "on_yellow")
    print(text)


if __name__ == "__main__":
    main()
