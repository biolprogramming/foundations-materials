#!/usr/bin/env python


def function1(arg):
    if arg <= 2:
        result = arg * arg
    else:
        result = arg + arg
    return result


def main():
    result = function1(2)
    print(result)


if __name__ == "__main__":
    main()