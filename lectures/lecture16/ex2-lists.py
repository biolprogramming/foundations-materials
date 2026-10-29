# LISTS

my_string = "this is my string"
my_list = my_string.split(" ")
print(my_list)

# we can access items
print(my_list[0])
print(my_list[1])

# we can slice
print(my_list[2:4])

# we can create lists
my_list = ['dog', 'cat', 'mouse', 'rat']

# we can also listify a string
my_list = list("dog")

# lists can be nested
my_list = [[1,2,3], ["cat", "dog"], [4.6]]
# access each nested list
my_list[0]
my_list[1]
my_list[2]
# access the 1st item of the 0th list
my_list[0][1]

# lists are mutable
my_list = ["dog", "cat", "mouse", "rat"]
my_list[1]
# now set my_list[1] to "hamster"
my_list[1] = "hamster"

# what happens here?
something = my_list.pop(2)
print(my_list)

# you can add lists
new_list = ["a", "b", "c"] + [1, 2, 3]

# you can multiply lists
new_list = ["a"] * 6

# lists are also objects and have methods
my_list = []
my_list.append(1)
print(my_list)
my_list.append(3)
print(my_list)
my_list.append(5)


# extend is also useful
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_1.extend(list_2)

# sort is another useful method
list_1 = ["z", "b", "a", "n", "m"]
list_1.sort()
print(list1)

# you can also join back together list components:
list_1 = ["z", "b", "a", "n", "m"]
"".join(list_1)
# or join with commas
",".join(list_1)