#!/usr/bin/env python3
"""
Will print ASCII art to the terminal based on the input given
@author Ellery Penas
@version 2018.04.18
"""
from termcolor import colored
from pyfiglet import Figlet as fig


def main():
    """main line function"""
    # dir() will print out all the functions within an object
    # print(dir(termcolor))
    # help(termcolor)

    #text = colored("hello", "red", "on_yellow")
    # print(text)
    f = fig(font="slant")
    ascii_art = f.renderText(text="Right Solutions Group")
    print(ascii_art)
    colored_art = colored(ascii_art, "red", "on_yellow")
    print(colored_art)


if __name__ == "__main__":
    main()
