# Reading files

# we use the open() function open files for reading/writing/etc.  Here, we open in read mode:
my_file = open("example1.txt", "r")
# let's see the type
type(my_file)

# we can read the file using several different methods.  first .read() the entire file:
text = my_file.read()
# after we read a file, we need to close it:
my_file.close()

# we can use readline to read the file line by line:
my_file = open("example1.txt", "r")
my_file.readline()
my_file.readline()
my_file.readline()
my_file.close()

# we can use .readlines()
my_file = open("example1.txt", "r")
text = my_file.readlines()
my_file.close()

# we can treat the file as an iterator:
my_file = open("example1.txt", "r")
for line in my_file:
    print(line)
my_file.close()

# The with keyword is really helpful because it alleviates the need for all this opening and closing:
with open("example1.txt", "r") as infile:
    for line in infile:
        print(line[::-1])

# WRITING a file
my_text = "this is my file\ni do not want it to be big\nnor do i want it to be small"
my_output_file = open("text-output.txt", "w")
my_output_file.write(my_text)
my_output_file.close()

# .writelines is the writing corollary of .readlines:
my_lines = ["this\n", "that\n", "the other\n"]
my_output_file = open("text-output.txt", "w")
my_output_file.writelines(my_lines)
my_output_file.close()

# again, we can use with to help deal with the opening and closing:
my_text = "this is my file\ni do not want it to be big\nnor do i want it to be small"
with open("text-output.txt") as my_output_file:
    my_output_file.write(my_text)

# what about something like this:
my_range = range(0,15)
with open("text-output.txt", "w") as my_output_file:
    for item in my_range:
        my_output_file.write(item)

# ah, ok - it has to be a string:
my_range = range(0,15)
with open("text-output.txt", "w") as my_output_file:
    for item in my_range:
        my_output_file.write(f"{item}")
# what did i forget??

# we can read and write at the same time:
with open("example1.txt", "r") as my_input:
    with open("text-output.txt", "w") as my_output:
        for line in my_input:
            my_output.write(f"{line[::-1]}")