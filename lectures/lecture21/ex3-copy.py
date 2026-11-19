# Copy

my_list = [1, 2, 3, 4]
my_other_list = my_list
print(my_other_list)

my_list[1] = 'gremlins'
# now check this out:
print(my_other_list)

# this happens because both variable names are pointing to the same
# location in memory that stores this result.  we can see that location
# like so (the hex command just makes this memory location easier to see)
hex(id(my_list))
hex(id(my_other_list))

# so how to we make a real copy?
import copy
my_list = [1,2,3,4]
my_other_list = copy.copy(my_list)
hex(id(my_list))
hex(id(my_other_list))

my_list[1] = 'gremlins'
print(my_list)
print(my_other_list)

# that makes what is known as a "shallow" copy of the list - check this out:
my_list = [1, ['gremlins', 'are', 'bad'], 3, 4]
my_other_list = copy.copy(my_list)

hex(id(my_list))
hex(id(my_other_list))

my_list[1][0] = 'cats'
print(my_list)
print(my_other_list)

# hmm, let's check the memory address of the [1] item:
hex(id(my_list[1]))
hex(id(my_other_list[1]))

# shoot - this is annoying.  to get a deepcopy of a list, we want to use copy.deepcopy()
my_list = [1, ['gremlins', 'are', 'bad'], 3, 4]
my_other_list = copy.deepcopy(my_list)
my_list[1][0] = 'cats'
print(my_list)
print(my_other_list)

hex(id(my_list[1]))
hex(id(my_other_list[1]))

