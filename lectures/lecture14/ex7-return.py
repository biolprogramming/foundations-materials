#!/usr/bin/env python


def abs_value(x):
    if x < 0:
        return -x
    if x > 0:
        return x


def main():
    result = abs_value(2)
    print(result)


if __name__ == "__main__":
    main()