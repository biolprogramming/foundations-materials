from Bio import Seq

# create a sequence object
my_seq = Seq.Seq("AGTACACTGGT")

my_seq
print(my_seq)

# check the different methods of this sequence object
dir(my_seq)

my_seq = Seq.Seq("AGTACACTGGT")
# get length
len(my_seq)

# iterate over nucleotides:
my_seq = Seq.Seq("AGTACACTGGT")
for nucleotide in my_seq:
    print(nucleotide)


# we can do other string-like things:
my_seq = Seq.Seq("AGTACACTGGT")

# get the first base
my_seq[0]

# slice from the 0th to the 5th base:
my_seq[0:5]

# reverse
my_seq[::-1]

# test for membership
"ACA" in my_seq

# or:
if "ACA" in my_seq:
    print("ACA is present")
else:
    print("ACA is not present")

# count the number of bases:
my_seq.count("A")

# lowercase:
my_seq.lower()

# but there are some string-like things we cannot do
# because these are sequences, not strings:
my_seq.titlecase()

# we can convert sequence objects to strings if we 
# need to, e.g.
str(my_seq).title()

# we can do things like add sequences:
seq_of_As = Seq.Seq("AAAA")
seq_of_Ts = Seq.Seq("TTTT")

# add them:
seq_of_As + seq_of_Ts

# add slices of each
seq_of_As[:2] + seq_of_Ts [0:2]


## Sequence objects have their own methods
## (that make sense given what they are...)

# get the complement
my_seq.complement()

# get the reverse complement
my_seq.reverse_complement()

# transcribe the sequence to RNA
my_seq.transcribe()

# translate the sequence:
my_seq.translate()

# notice the error here... let's fix that:
my_seq = Seq.Seq("AUGAGTACACTGGTGTGA")
# take a look at the result
my_seq

# you can even do stuff like change the translation table
# this uses NCBI translation table identifiers...
# https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi
my_seq.translate(table=2)

# if for some reason you need to see the coding tables:
from Bio.Data import CodonTable
standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
print(standard_table)


## SeqIO
# This is the module for reading and writing different sequence files
from Bio import SeqIO
with open("my_file.fasta", "r") as infile:
    for record in SeqIO.parse(infile, 'fasta'):
        print(record)

# As with file reading, there are other ways to read in a file.
# You can read an entire file at once:
with open("my_file.fasta", "r") as infile:
    record = SeqIO.read(infile, "fasta")
    # notice that this fails because there is
    # > 1 record in the file

# We can try that with only a single record:
with open("caligus-clemensi-COI.fasta", "r") as infile:
    record = SeqIO.read(infile, "fasta")

# we can also read an entire file and make it a dict()
with open("my_file.fasta", "r") as infile:
    record = SeqIO.to_dict(SeqIO.parse(infile, "fasta"))


# let's go back to standard example using iterator:
with open("my_file.fasta", "r") as infile:
    for record in SeqIO.parse(infile, 'fasta'):
        print(record)

# what is this sequence object that gets created
# and that we call "record"
# let's look at it:
record

# we can access the sequence data like so:
record.seq

# but we can access the other attributes, as well:
record.id
record.name
record.description

# let's look at a real example
with open("matts_file.fasta", "r") as infile:
    for record in SeqIO.parse(infile, 'fasta'):
        print(record)

# we can access the sequence data like so:
record.seq

# but we can access the other attributes, as well:
record.id
record.name
record.description

# sequence records also have a "format" method, so you can
# change their output format:
record.format("fasta")

# and if we want to see what that looks like when printed to the screen:
print(record.format("fasta"))

# and if we want some other type of format, we change the format specifier.
# that said, the new format has to make sense for the data type. So:
print(record.format("tab"))

# we can also read data like fastq files:
with open('my_file.fastq', 'r') as infile:
    for fastq in SeqIO.parse(infile, "fastq"):
        print(fastq)

# We can write sequences out:
from Bio import Seq
from Bio import SeqRecord
from Bio import SeqIO

seq_string = 'ACGTACGT'
seq_object = Seq.Seq(seq_string)
seq_record = SeqRecord.SeqRecord(
    seq_object, 
    id="my_first_seq",
    name="",
    description=""
)

with open('my_first_file.fasta', 'w') as outfile:
    outfile.write(seq_record.format('fasta'))


# here is a pretty commong programming pattern
# that converts a fastq to a fasta
with open('my_file.fastq', 'r') as fq:
    with open('my_converted_file.fasta', 'w') as fa:
        for record in SeqIO.parse(fq, 'fastq'):
            fa.write(record.format('fasta'))