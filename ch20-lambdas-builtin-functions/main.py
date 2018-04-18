#!/usr/bin/env python3
"""
Chapter 20 - Lambdas and builtin functions
@author Ellery Penas
@version 2018.04.07
"""
import sys


def main():
    """main line function"""
    # Normal function definetion
    def square(x):
        return x * x

    # lambda version of the same function
    # square2 = lambda num: num * num

    print(square(4))
    # print(square2(5))

    # more lambda fun and using the map function to affect items in a list
    nums = [1, 2, 3, 4, 5]
    dubs = list(map(lambda x: x * 2, nums))

    print(dubs)  # [2, 4, 6, 8, 10]

    # a look at the keyword 'all'; all items must be True to return True
    print(all([0, 1, 2, 3]))  # False

    nums = [2, 4, 6, 8]
    print(all([num for num in nums if num % 2 == 0]))  # True

    # a look at the keyword 'any'; at least 1 item in the collection must be
    # true
    names = ['Jill', 'Jen', 'Dave', 'Don']
    print(any([name[0] == 'J' for name in names]))

    # genex vs list comprehension
    list_comp = sys.getsizeof([x * 10 for x in range(1000)])
    genex = sys.getsizeof(x * 10 for x in range(1000))

    print(f"This the size of a list comp element in memory: {list_comp} BYTES")
    print(f"This the size of a genex element in memory: {genex} BYTES")


if __name__ == "__main__":
    main()
