#!/usr/bin/env python


def function1(arg):
    product =  arg * arg
    return arg, product


def main():
    result = function1(10)
    print(type(result))
    print(result)


if __name__ == "__main__":
    main()