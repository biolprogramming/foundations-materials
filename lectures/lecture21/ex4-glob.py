# Glob

# when we have files that we want to get (and possibly filter), we can use the glob module:
import glob
# now get All files in `example-files`
all_files = glob.glob("example-files/*")

# sometimes we want to filter:
all_files = glob.glob("example-files/*.fastq")
# now we can do stuff with these (this is a list), e.g.:
for file in all_files:
    print(file)

# how might we get ALL fasta AND fastq files?
all_files = glob.glob("example-files/*.fast*")

# when you use the full path with glob, you get the full path in the results
all_files = glob.glob("/workspaces/foundations-2024-lectures-found-class-template/Lecture-17/example-files/*.fast*")

# glob is dumb, so you cannot do things like combine multiple wildcards with an "and" or an "or"....