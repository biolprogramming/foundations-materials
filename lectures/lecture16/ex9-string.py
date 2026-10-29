#!/usr/bin/env python
# note that this is not formatted correctly - during class i was pasting
#  many of these into ipython to show what they do.

# reverse a string
my_string = "Able was I were I saw Elba"
print(my_string[::-1])

# find length of a string
len(my_string)

# access elements of a string:
my_string = "gorilla"
my_string[0:2]
# this is the same as the above:
my_string[:2]
# get the last character
my_string[-1]
# here's another slice
my_string[1:5]
# and another one
my_string[-6:-2]

# strings are immutable
my_string = "gorillas like bananas"
my_string[0:8] = "monkeys"
# so we can't change the string directly, we have to do that indirectly
my_new_string = "monkeys" + my_string[8:]
print(my_new_string)

# string methods
my_string = "gorillas"

# we can uppercase
my_string.upper()

# we can see all of these methods using "dir"
dir(my_string)

# some of these are realy handy:
my_string = "this is my string"
# count letters
my_string.count("i")
# find words
my_string.find("my")

# split strings
my_string.split(" ")

# can be helpful for delimited files:
my_line_1 = "index,name,species,quantity"
my_line_2 = "A2455,bob,canis,2"
my_line_3 = "A2456,steve,felis,1"

# we can easily remove line endings and other crud
my_string = "   this is my string\n"
my_string.strip()

# we can test for membership:
my_string = "this is a good string"
"good" in my_string

# we can compare strings
my_string == "this is a good string"
my_string == "dogs"