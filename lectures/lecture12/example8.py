#!/usr/bin/env python

# THIS IS A VOID FUNCTION
def first_fname(arg1):
    """function description"""
    print(arg1+arg1)


# THIS IS A FRUITFUL FUNCTION
def second_fname(arg1):
    """function description"""
    result = arg1+arg1
    return result

#look at:
first_fname(2)
# versus:
result_from_function = second_fname(2)
print(result_from_function)
