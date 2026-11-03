#!/usr/bin/env python


def function1(arg):
    product =  arg * arg
    return arg, product, arg


def main():
    r_arg1, product, r_arg2 = function1(10)
    print(r_arg1)
    print(product)
    print(r_arg2)
    


if __name__ == "__main__":
    main()