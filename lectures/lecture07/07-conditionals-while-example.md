# Lecture 07

## if, elif, else

You can also add a third category of conditions in the form of `elif`, which is read "else if".  These are conditions that fall between the `if` and `then`, and you can have as many as you like of these:
```bash
my_number=2
if [ $my_number = 1 ]; then
  echo "my number is 1";
elif [ $my_number = 2 ]; then
  echo "my number is 2";
elif [ $my_number = 2 ]; then
  echo "my number is 3";
else
  echo "my number is 4";
fi
```
Notice that this evaluates each of the conditions, in turn, until it reaches a satisfactory conclusion.  That said, check this out:
```bash
my_number=10
if [ $my_number = 1 ]; then
  echo "my number is 1";
elif [ $my_number = 2 ]; then
  echo "my number is 2";
elif [ $my_number = 2 ]; then
  echo "my number is 3";
else
  echo "my number is 4";
fi
```
Is that correct?

## Checking for > and <

In `bash`, checks for equality use `=`, as you've seen above.  However, you often test for things like `>`, `<`, `>=`, and `<=`, and there are an entire family of text shortcuts for these (also so you don't have to worry about escaping them).  You can read about all of these in the [advanced scripting guide for bash](https://tldp.org/LDP/abs/html/comparison-ops.html), but the important ones are: `-eq, -ge, -gt, -le, -lt`, which stand for "equality", "greater than or equal", "greater than", "less than or equal", and "less than".  They work mostly like you would expect:
```bash
my_number=10
if [ $my_number -lt 5 ]; then
  echo "my number is less than 5";
else
 echo "my number is greater than 5";
fi
```

## Using conditionals in a loop

Here's a conditional statement used inside of a loop (don't forget to keep an eye on the required spaced inside the `[]`!):
```bash
for i in {1..50}; do
  if [ $i -le 25 ]; then
    echo "$i is <= 25";
  else
    echo "$i > 25";
  fi
done
```

## Building a program from pieces (and the weird modulo operator)

What does the following do?  And, what is the `%` operator:
```bash
for i in {1..50}; do
  result=$(($i % 2));
  if [ $result -ne 0 ]; then
    echo $i "odd";
  else
    echo $i "even";
  fi
done
```

## While loops

It's also possible to write `while` loops in `bash`.  IMO, these are not quite as easy to control in `bash` because you need to reach a specific ending point for the while loop to stop running, and it's sometimes easy to forget the ending condition, which means the loop runs continously until you stop it (that said, somethimes this is what you WANT to do).  Here's an example of what these sorts of loops look like:
```bash
i=0
while [ $i -lt 50 ]; do
  echo $i
  (( i++ ))
done
```
This same thing can also be accomplished with:
```bash
i=0
while [ $i -lt 50 ]; do
  echo $i
  i=$(( $i+1 ))
done
```

And we can do our even/odd computation the same way
```bash
i=0
while [ $i -le 50 ]; do
  result=$(($i % 2));
  if [ $result -ne 0 ]; then
    echo $i "odd";
  else
    echo $i "even";
  fi
  i=$(( $i+1 ))
done
```

## example

In the `files` directory is a file named `first50_250bp.bp`. Let's take a look at it.... What we're going to do is manipulate this file in a number of ways.

1. First, let's file all sequences that start w/ `AA` using a loop
2. Let's write these to a new file
3. Is there another way that we can do the same thing (not using a loop)

## awk

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
What is we want columns 1 and 3?
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
How about this?
```bash
awk 'NR > 1 && $5 != "NA" && $5 > 17 {print $1, $5}' birds.tsv
```
