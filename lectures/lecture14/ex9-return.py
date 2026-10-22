#!/usr/bin/env python


def function1(arg):
    if arg <= 2:
        product = arg * arg
        return product
    else:
        summ = arg + arg
        return summ
    print("This will never run!")


def main():
    result = function1(2)
    print(result)


if __name__ == "__main__":
    main()