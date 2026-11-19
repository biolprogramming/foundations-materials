# There are many ways to format strings in python.

# The first is the very old way, using % signs, like so:
my_name = "brant"
work_at = "LSU"
print("My name is %s and I work at %s" % (my_name, work_at))

# You have some control over formatting
my_name = "brant"
my_float = 3.142
print("My name is %s and I work at %.1f" % (my_name, my_float))

# The older string formatting was replaced with the .format() method:
my_name = "brant"
work_at = "LSU"
print("My name is {0} and I work at {1}".format(my_name, work_at))

# You can easily repeat things:
print("My name is {0} and I work at {1} {1} {1}".format(my_name, work_at))
# Or
print("My name is {0} and I work at {1}. {1} is a nice place to work, expecially for a person named {0}.".format(my_name, work_at))

# If you don't need to make any repeats, you can substitute implicitly:
print("My name is {} and I work at {}.".format(my_name, work_at))

# you can also temporarily "rename" variable to make things clearer:
print("My name is {name} and I work at {work}".format(name=my_name, work=work_at))

# and .format() lets' you use dictionaries:
details = {"my_name":"brant", "work_at":"LSU"}
print("My name is {my_name} and I work at {work_at}. {work_at} is a nice place to work".format(**details))
# the ** basically turns the dictionary into:
# .format(my_name="brant", work_at = "LSU")

# like with percent formatting, you can specify field types like so (there's a large
# specification language you can read more about here: https://docs.python.org/3/library/string.html#format-specification-mini-language
my_int = 42
my_float = 3.142
print("Here is an int {:d} and a float {:.2f}".format(my_int, my_float))

# you can easily format big numbers prettily:
million=1000000
print("Here's how you format {:,d}".format(million))

# finally there are fstrings, which are "new" and basically replace everything else:
my_name = "brant"
work_at = "LSU"
print(f"My name is {my_name} and I work at {work_at}")

# these can even include operations/code like:
print(f"The result is {8+8}")

# you can include methods them:
my_name = "brant"
# use the "upper" method of a string
print(f"My name is {my_name.upper()}")

# you can still use the formatting mini language:
million=1000000.696584696
print(f"Here's how you format {million:,.2f}")

# you can have multiline fstrings:
# you can have multiline fstrings
my_name = "brant"
position = "associate professor"
institution = "LSU"
message = (
    f"Hello, my name is {my_name}. "
    f"I am a {position}. "
    f"At {institution}."
)
print(message)