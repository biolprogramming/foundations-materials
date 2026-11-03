# Dictionaries

my_dict = {1:"dogs", 2:"cats", 3:"mice"}
print(my_dict)
# we can access the first element
my_dict[1]
# but keys that do not exist do not work:
my_dict[0]

my_dict = {0:"dicts", 1:"are", 2:"pretty", 3:"cool"}
# the keys can be pretty much anything we want:
my_dict = {"word1":"dicts", "word2":"are", "word3":"pretty"}
my_dict["word1"]

# we can make an empty dict pretty easily
my_pets = dict()
# or
my_pets = {}
# and we can add keys+values
my_pets["dogs"] = 2
print(my_pets)
# we can change this element
my_pets["dogs"] = 12
print(my_pets)
# we can also increment this element
my_pets["dogs"] += 1
print(my_pets)
# and we can delete an element
my_pets = {"dogs": 2, "cats":3, "hamsters":1}
del my_pets["dogs"]
print(my_pets)

# keys must be unique and values can be anything:
my_pets = {"dogs":["scoobie", "idiot"],
 "cats":["stinker", "sir poopsalot"]}
# here are values of different types:
import numpy
my_pets = {"dogs":numpy.array([1,2,3]),
 "cats": 12}

# dictionaries are unordered:
test_dict = {"A": "best", "B": "good", "C": "okay", "D": "bad"}

# we can get the length of a dictionary:
my_pets = {"dogs":["scoobie", "idiot"],
 "cats":["stinker", "sir poopsalot"]}
len(my_pets)

# we can iterate over a dictionary:
for item in my_pets:
    print(item)

# if we also want the value that goes along with the key:
for item in my_pets:
    print(item, my_pets[item])

# but we can also do this which is faster:
for k, v in my_pets.items():
    print(k, v)

my_pets = {"dogs": 2, "cats":3, "hamsters":1}
# we can get onlt the keys
my_pets.keys()
# or only the values
my_pets.values()