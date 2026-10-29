# Tuples

my_tuple = ("this", "is", "my", "tuple")
type(my_tuple)

print(my_tuple[1])

# this created a tuple
my_tuple = ()

# we can tuplify a string:
my_tuple = tuple("dog")
# or a list
my_list = ["dog", "cat", "rat"]
my_tuple = tuple(my_list)

# to create a tuple, a single element must be followed by a comma
# so, not a tuple
not_a_tuple = ("a")
type(not_a_tuple)

is_a_tuple = ("a", )
type(is_a_tuple)

# tuples are immutable:
my_tuple = ("dog", "cat", "mouse", "rat")
my_tuple[1] = "hamster"

# you cannot modify tuple elements... but what about this?
my_tuple = ([1,2,3], ["cat","dog"], [4.6])
my_tuple[1][0] = "rabbit"
print(my_tuple) 

# you can add tuples:
tuple1 = ("a", "b", "c")
tuple2 = ("1", "2", "3")
tuple1 + tuple2
# you can also mutiply tuples:
("a", ) * 10