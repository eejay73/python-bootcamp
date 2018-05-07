#!/usr/bin/env python3
"""
Chapter 23 - Object Oriented Programming (OOP)
@author Ellery Penas
@version 2018.04.25
"""


class User:
    # Class variables can be accessed directly from the Class and not in all
    # instance
    active_users = 0

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    # first instance method for Class User
    def fullname(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."

    # always pass self as the first parameter within an instance method
    def likes(self, thing):
        return f"{self.first} likes {thing}"


def main():
    """main line function"""
#    print(user1.first + " " + user1.last)
#    print(user1.fullname())
#    print(user1.initials())
#    print(user1.likes("chips"))
    print(User.active_users)
    user1 = User("Bill", "Kill", 15)
    user2 = User("John", "Smith", 71)
    print(User.active_users)


if __name__ == "__main__":
    main()
