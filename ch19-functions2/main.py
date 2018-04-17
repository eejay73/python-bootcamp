#!/usr/bin/env python3
"""
Bootcamp Chapter 19 - Functions 2
@author Ellery Penas
@version 2018.04.18
"""


def main():
    """main line function"""
    def sum_all_nums(*args):
        """
        Function to help explain unpacking tuple args
        """
        print("The value of args is: ", args)
        total = 0
        for num in args:
            total += num
        return total
    # sum_all_nums(1,2,3,4,5)

    # num = [1, 2, 3, 4, 5, 6]
    # print(sum_all_nums(*num))  # add a * to the arg to unpack a list or tuple

    def display_names(first, second):
        print('{} says hello to {}'.format(first, second))

    names = {"first": "EJ", "second": "Jen"}
    # display_names(names) # nope....
    display_names(**names)  # to unpack a dict use ** in fromt of arg


if __name__ == "__main__":
    main()
