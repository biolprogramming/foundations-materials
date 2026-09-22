# awk

Built into Linux/Unix are several programs that are very useful for filtering or modifying **tabular** data. One of those programs is named `awk` - and it's pretty compact, has a weird syntax, but is extremely powerful for doing many manipulations on a tabular data file really quickly.  Let's go look at some of these tabular data, which are in `files/birds.tsv` and `files/birds.csv`.  The first:
```txt
sample_id	species	sex	site	mass_g	wing_mm	tarsus_mm	plumage
MAN001	Manacus_manacus	M	Panama	16.2	52.1	20.3	white
MAN002	Manacus_manacus	F	Panama	17.8	53.4	20.9	olive
MAN003	Manacus_manacus	M	Panama	15.9	51.8	19.8	white
MAN004	Manacus_vitellinus	M	Panama	16.5	52.9	20.1	yellow
MAN005	Manacus_vitellinus	F	Panama	18.1	54.0	21.2	olive
MAN006	Manacus_vitellinus	M	Colombia	NA	52.5	20.0	yellow
MAN007	Manacus_manacus	F	Colombia	17.2	53.1	20.7	Olive
COL001	Colinus_virginianus	M	Louisiana	172.4	112.3	31.5	brown
COL002	Colinus_virginianus	F	Louisiana	168.9	110.8	30.9	brown
COL003	Colinus_virginianus	M	Texas	181.0	114.1	32.2	brown
COL004	Colinus_virginianus	F	Texas	NA	111.5	31.0	Brown
COL005	Colinus_virginianus	M	Louisiana	175.3	113.0	31.8	brown
```
and the second:
```txt
sample_id,species,sex,site,mass_g,wing_mm,tarsus_mm,plumage
MAN001,Manacus_manacus,M,Panama,16.2,52.1,20.3,white
MAN002,Manacus_manacus,F,Panama,17.8,53.4,20.9,olive
MAN003,Manacus_manacus,M,Panama,15.9,51.8,19.8,white
MAN004,Manacus_vitellinus,M,Panama,16.5,52.9,20.1,yellow
MAN005,Manacus_vitellinus,F,Panama,18.1,54.0,21.2,olive
MAN006,Manacus_vitellinus,M,Colombia,NA,52.5,20.0,yellow
MAN007,Manacus_manacus,F,Colombia,17.2,53.1,20.7,Olive
COL001,Colinus_virginianus,M,Louisiana,172.4,112.3,31.5,brown
COL002,Colinus_virginianus,F,Louisiana,168.9,110.8,30.9,brown
COL003,Colinus_virginianus,M,Texas,181.0,114.1,32.2,brown
COL004,Colinus_virginianus,F,Texas,NA,111.5,31.0,Brown
COL005,Colinus_virginianus,M,Louisiana,175.3,113.0,31.8,brown
```
Notice that the different between the two are the separators of the columns. Ok, so if we simply wanted to filter the data in these files by the `sample_id`, let's say we want to extract all `manacus` individuals, what could we do?

How about if we want to filter on other columns??? That's where `awk` comes in. Like I said, the syntax gets a little rough...

Let's say we want to extract only the first and second column of these data:
```bash
awk '{print $1 $2}' files/birds.tsv
```
Hmmm, that's not quite correct... what have we lost? Ok, so let's try:
```bash
awk '{print $1, $2}' files/birds.tsv
```
Notice that this is also the same as:
```bash
awk '{print $1, $2}' < files/birds.tsv
```
As well as the same as:
```bash
cat files/birds.tsv | awk '{print $1, $2}'
```
What if we want columns 1 and 3?
```bash
awk '{print $1, $3}' files/birds.tsv
```
Or, 1, 2, 3, 4?
```bash
awk '{print $1, $2, $3, $4}' files/birds.tsv
```
How about if we want to use awk with the CSV file?
```bash
awk '{print $1, $2}' files/birds.csv
```
Is that correct? Why not....?
```bash
awk -F ',' '{print $1, $2}' files/birds.csv
```
Ok - that seems to mostly work... but look at the output:
```
sample_id species
MAN001 Manacus_manacus
MAN002 Manacus_manacus
MAN003 Manacus_manacus
MAN004 Manacus_vitellinus
MAN005 Manacus_vitellinus
MAN006 Manacus_vitellinus
MAN007 Manacus_manacus
COL001 Colinus_virginianus
COL002 Colinus_virginianus
COL003 Colinus_virginianus
COL004 Colinus_virginianus
COL005 Colinus_virginianus
```
What is sort of wrong here? `-F` sets the input separator, but we also need to set the output separator:
```bash
awk -F ',' -v OFS=',' '{print $1, $2}' files/birds.csv
```
Also note that `-F ','` is a shortcut for `-v FS=','`, so you could do:
```bash
awk -v FS=',' -v OFS=',' '{print $1, $2}' files/birds.csv
```
The `-v` is setting an AWK variable - in this case the input and output separators.

## awk filtering

You might want to drop the header and then filter on specific values.  So, to drop the header is:
```bash
awk 'NR > 1' files/birds.tsv
```
And we might want to filter on columns `species` and `site`, which we could do with something like:
```bash
awk '$2 ~ /^Manacus/ && $4 == "Panama"' files/birds.tsv
```
What if we want to filter, but also want to only keep certain values?
```bash
awk '$2 ~ /^Manacus/ && $4 == "Panama" {print $1, $3, $5}' files/birds.tsv
```
Here is another filtering example... but keep a close eye on it:
```bash
awk 'NR > 1 && $5 > 100 {print $1, $5}' files/birds.tsv
```
So, how do we fix this...
```bash

```
What about "or"? In `awk`, we specify an "or" with two pipes `||`:
```bash
awk '$2 ~ /^Manacus/ || $4 == "Louisiana" {print $1, $3, $5}' files/birds.tsv
```

## awk arithmetic
Ok, so how about this:
```bash
awk -F'\t' 'NR > 1 && $5 != "NA" {printf "%s\t%.3f\n", $1, $5 / $7}' files/birds.tsv
```
What if I wrote it like this:
```bash
awk -F'\t' 'NR > 1 && $5 != "NA" {printf "%s\t%.4f\n", $1, $5 / $7}' files/birds.tsv
```
Or, like this:
```bash
awk -F'\t' 'NR > 1 && $5 != "NA" {printf "%.4f\t%s\n", $5 / $7, $1}' files/birds.tsv
```

# sed
There is another program that you see used on the command line quite often, and that is `sed`. `sed` is sort of similar to `awk` in that it can modify data, but it is really **ONLY** meant for modifying data (versus filtering those data). In fact, `sed` stands for "stream editor". In my mind, `sed` is mean for pretty quick modfications... although because it operates line-by-line, it can make those modifications to ENORMOUS files.  Let's see how it works.

`sed` can print only certain lines - this prints only lines 2,3,4:
```bash
sed -n '2,4p' files/birds.tsv
```
`sed` can also make **universal** substitutions - so replace ALL NA values with `.`, which is sometimes a standard convention:
```bash
sed 's/NA/./g' files/birds.tsv
```
And if we wanted to save that result, we could output it to a new file:
```bash
sed 's/NA/./g' files/birds.tsv > files/birds.MOD.tsv
```
We can also use `sed` to help cleanup data. What do you think this is going to do?
```bash
sed 's/\tOlive$/\tolive/; s/\tBrown$/\tbrown/' files/birds.tsv
```
How about this?
```bash
sed 's/_/ /' files/birds.tsv
```
Notice that the above command will only replace the **first** instance of a `_` that it finds.  If you want to replace ALL of them, you need to add the "global" flag:
```bash
sed 's/_/ /g' files/birds.tsv
```
This is exactly how you can use `sed` to convert a TSV file to a CSV file:
```bash
sed 's/,/\t/g' files/birds.csv
```
`sed` can also be a pretty blunt tool - imagine we had another file `birds2.tsv`, what happens when we run the command like the one above??
```bash
sed 's/NA/./g' files/birds2.tsv 
```
You very often see `sed` used to manipulate sequence (FASTA) files.  For instance, let's add some characters to the header of our `first50_250bp.fasta` file:
```bash
sed 's/^>/>Scaffold_/' files/first50_250bp.fa
```
Let's save that file:
```bash
sed 's/^>/>Scaffold_/' files/first50_250bp.fa > files/first50_250bp.MOD.fa
```
Now, if we want to reverse what we did:
```bash
sed 's/^>Scaffold_/>/' files/first50_250bp.MOD.fa
```

# Other tricks of the trade
Lots of times you can use trick that we've learned to do useful things (very quickly). for instance, how could I count all the sequences in `first50_250bp.fa`?
```bash

```
Ok, how about counting the number of sequences in a fastq file?
```bash

```
But, what if i told you this...
```bash

```
So, we would be better off doing something like counting all lines and dividing by 4... which we can do in 2 ways:
```bash
awk 'END {print NR/4}' files/test.fastq
# or
echo $(( $(wc -l < files/test.fastq) / 4 ))
```

# Compressing and archiving
One command we have not talked about yet is `gzip` and `gunzip`, which compress and decompress files (respectively). Often, fastq files come this way and you REALLY do not want to decompress them because they're huge.  So you can do something like this:
```bash
gunzip -c files/test2.fastq.gz | wc -l
# OR\
echo $(( $(gunzip -c files/test2.fastq.gz | wc -l) / 4 ))
```
We also have not talked about `tar` yet. `tar` is a name for a program that is based off of how we once, generally, store backup data - on tape archives. So, `tar` the command really means `tape archive`. What `tar` does, in practice, is help to group together and compress multiple files and directories.

Let's take a look in `files-2`.  There are lots of files within this directory, and if we try something like `gzip`, it will not work:
```bash
gzip files-2
gzip: files-2 is a directory
```
So, in order to compress this directory (and the files within it), we need to use `tar`. `tar` has lots of flags, but the important ones are `-czf` which create the directory, compress the directory with `gzip`, then name the file whatever follows.  So, you run it like this:
```bash
tar -czf files-2.tar.gz files-2
```
Now, you can get rid of the original:
```bash
rm -r files-2
```
And, if you want, reconstitute everything by **decompressing** the archive:
```bash
tar -xzf files-2.tar.gz
```
If you'd like to see what `tar` is doing, you can also add the `-v` flag for "verbose" output.
```bash
tar -xzvf files-2.tar.gz
```
One quick note, sometimes people compress files with programs like `bzip` instead of `gzip`. In that case the archives are `bz2` and have names like `<some-file>.tar.bz2`. In that case you cannot decompress with `bzip` because the file is a `gzip`. So, you need a different flag:
```bash
# create a bzip2 archive:
tar -cjf files-2.tar.bz2 files-2/

# decompress a bzip2 archive:
tar -xjf files-2.tar.bz2
```
There are other handy tools you can use like `md5sum`. `md5` is an algorithm that computes what's known as a "message digest fingerprint" for a given file.  This is also called a "checksum". Once you have a checksum for a file, you can use that checksum to see if the file has changed from one version to another.

Let's get the checksum of `test.fastq`:
```bash
md5sum files/test.fastq
a3b6951aedd7237a4c27a7e027ba2370  files/test.fastq
```
Notice that we can make a copy of that file (without modifying anything), and then take a look at the modified files checksum:
```bash
cp files/test.fastq files/test2.fastq
# now get checksum:
md5sum files/test2.fastq
a3b6951aedd7237a4c27a7e027ba2370  files/test2.fastq
```
Notice that those two checksum values are the same.  Now, let's modify the `files/test2.fastq` slightly.  Use nano to edit the first line.
```bash
nano files/test2.fastq
md5sum files/test2.fastq
7266d9285d3dc0dfe6f33c12e84a377b  files/test2.fastq
```

# Comparing
There's actually a really handy program that let's us do stuff like check to see **HOW** two files are different, and that's called `diff`. It has a pretty complicated syntax - so you'll want to read more about it if you want to use it.  But let's take a look at our original versus our modified file:
```bash
diff files/test.fastq files/test2.fastq
```
