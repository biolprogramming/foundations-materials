#!/usr/bin/env python


def fname(arg):
    """function description"""
    # this is an empty function
    pass


def example1():
    """reverse a string"""
    s = "this is my string"
    print("One way: ")
    print(''.join(reversed(s)))


def example2():
    """reverse a string another way"""
    s = "this is my string"
    print("Another way:")
    print(s[::-1])


example1()
example2()