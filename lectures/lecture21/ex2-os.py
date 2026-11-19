# the os module
# before we use, we need to import
import os

# the top level of the os module contains useful operating system commands:
# get some info about our environment (note that this is a method, not a function)
os.environ

# get the current working directory:
os.getcwd()

# change the cwd:
os.chdir()

# get operating system information:
os.uname()

# within the os module, there is the path submodule.  it works with paths
# get the absolute path from a relative path:
os.path.abspath("../../")

# join two paths:
os.path.join("/tmp", "folder")

# split a path into head and tail:
result = os.path.split("/tmp/dir/file1.py")
# access each part
result[0]
result[1]

# get the basename of a file (return filename from a path)
os.path.basename("/tmp/dir/file.txt")

# get the dirname of a file (return directory name from a path):
os.path.dirname("/tmp/dir/file.txt")

# get the root and extension of a path:
os.path.splitext("/tmp/dir/file.txt")

# get filename and extension from a path:
os.path.splitext(os.path.basename("/tmp/dir/file.txt"))