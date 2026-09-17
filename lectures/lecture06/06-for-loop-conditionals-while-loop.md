# Lecture 06

### Empty variables don't necessarily cause an error

Try this:
```bash
echo $blah.txt
```
Have you "declared" blah yet (e.g. `blah=<something`)?  No you haven't... but there's no error when you try to use it.

### You can do other string manipulations with variables

What follows are some of the most useful string manipulations - I use these all the time. Again, a nice pithy answer for how to do this is from (stackoverflow)[https://stackoverflow.com/questions/965053/extract-filename-and-extension-in-bash]:
```bash
filename_only=$(basename -- "$fullfile")
extension="${filename##*.}"
filename="${filename%.*}"
```
So, let's say you have some path to a file:
```bash
MY_PATH=/this/is/a/path/to/my/filename.txt
```
You can extract the component parts with:
```bash
filename=$(basename -- "$MY_PATH")
echo $filename_only

extension="${filename##*.}"
echo $extension

name="${filename%.*}"
echo $name
```

## Arithmetic in bash

### let
In `bash`, you can perform arithmetic -  but you can't do it quite like you think you can.  Try:
```bash
4+4
```
on the command line, and you'll get:
```bash
bash: 4+4: command not found
```
One way to perform arithmetic but to set the result to a value is using the command `let`.  For instance:
```bash
let a=4+4
```
How do we see the result?
```bash
echo $a
```
With `let` you also always have to set the result equal to some variable.

### expr
In order to perform arithmetic in `bash`, you can also use a special command called `expr`:
```bash
expr 4 + 4
```
Be sure to include the spaces between the **operator** or it won't work.


### $(( expression ))

You can also skip `let` and do arithmetic using `$(( expression ))`, like so:
```bash
$((4 + 4))
```
Whoops - if you want to just see this result, you need to use `echo` in from of the expression, so:
```bash
echo $((4 + 4))
```
Alternativelty, just like `let` you can set this result equal to a variable and then `echo` the variable:
```bash
a=$((4 + 4))
echo $a
```
With this form, we can also do things like exponentiation:
```bash
echo $((4**4))
```

### The ++ operator

From just above, `$a` should have a value of 8.  What happens if we:
```bash
(( a++ ))
```
Run:
```bash
echo $a
```
Do it again:
```bash
(( a++ ))
```
Run:
```bash
echo $a
```
So, what is the `++` doing here?

## Loops

Ok - now we're going to talk about something that people sometimes have conceptual difficulty understanding, and that is "looping".  In computer terms, a "loop" is when you tell the computer to do something over and over and over.  What the computer is "looping" over can be the numbers from 1 to 100, a list of files, to pretty much anything there is more than one of.

Let's start with a simple case - using some language that you not seen yet - what do you think this is going to do:
```bash
for i in {1..10}; do
  echo $i;
done
```
Ok, first, you have the structure of the command:
```bash
for <some stuff to loop over>; do
  <some things to do>;
done;
```
This is how `bash` loops are typically written. That said, you can put them all on one line like so:
```bash
for <some stuff to loop over>; do <some things to do>; done
```
This form can be harder to read.  NOTICE that every line or task in the loop ends with a semi-colon. You can have as many `<some things to do>` lines as you would like:
```bash
for <some stuff to loop over>; do
  <some things to do>;
  <other things to do>;
  <even more other things to do>;
  <even more more other things to do>;
done;
```

### Brace expansion

Ok, so back to our loop.  What does the `{1..10}` do?  Let's just see what happens on its own:
```bash
echo {1..10}
```
For `bash`, this is called "brace expansion", and it can be used for a lot of things.  Here, we're telling it to generate the values, 1 to 10 for us, so you should see:
```bash
1 2 3 4 5 6 7 8 9 10
```
Brace expansion can be really handy sometimes.  What do you think this will do:
```bash
echo a{d,c,b}e
```
Ok - how about this?
```bash
echo a{d,c,b}{g,f,i}
```
Sometimes you need to make lots of combinations of things.  Here's every combination of 1,2,3 in 3 positions:
```bash
{1,2,3}{1,2,3}{1,2,3}
```
### Back to loops

If we go back to our loop:
```bash
for i in {1..10}; do
  echo $i;
done
```
We are telling `bash` to generate these numbers, then loop over them, one by one, and print the value to the screen.  So, we see:
```bash
1
2
3
4
5
6
7
8
9
10
```
A more mathematical way to do this is also possible:
```bash
for ((i=1;i<=10;i++)); do
  echo $i
done
```
But, I actually like using the brace expansion better (it's cleaner).  You can also use the `seq` command to do exactly the same thing:
```bash
for i in $(seq 1 100); do
  echo $i;
done
```
But what's happening here?  What you are seeing in the `$(seq 1 100)` is what's known as a "command substitution", and it basically tells `bash` to run this first, then use the output from this command in the remaining `bash` code.  It's equivalent to first setting a variable to the sequence, then using the variable in the loop.  Being surrounded by `$()` basically means "execute this command".
```bash
values=$(seq 1 100)
for i in $values; do
  echo $i;
done
```
The nice thing about using `seq` is that you can make pretty complex sequences of numbers without having to thing about the math of it at all.  For instance, do you want to loop over numbers 1 to 100 by 4?  Ok!
```bash
for i in $(seq 1 4 100); do
  echo $i;
done
```

### Variable names in loop

Also not that you don't have to use `$i` as your variable - you can use whatever you like (`i` is just quick and easy to type):
```bash
for bob in $(seq 1 100); do
  echo $bob;
done
```
You can also iterate over lines in a file - let's try that really quickly.  Create a file (e.g. with `nano`) named `file1.txt` that contains:
```bash
word1
word2
word3
word4
word5
```
You can iterate over the contents of this file (line by line) like so:
```bash
for line in `cat file1.txt`; do
    echo $line;
done
```
Now that you've seen that, go ahead and delete the file:
```bash
rm file1.txt
```

### Doing other stuff in a loop

We can create a loop to output only the `*.mp3` filenames in `examples/lecture-5/files/`:
```bash
for file in `ls examples/lecture-5/files/*.mp3`; do
  echo $file;
done
```

### On the use of semicolon

Note that the folliwing are equivalent:
```bash
for file in `ls examples/lecture-5/files/*.txt`; do
  echo $file;
done
```
is the same as (notice that there is no semi-colon):
```bash
for file in `ls examples/lecture-5/files/*.txt`; do
  echo $file
done
```
That's annoying.  Also another inconsistency.


## Conditional statements

In addition to being able to do things like use `for` loops, `bash` allows you to use conditional statements within or outside of a loop to control what is happening.  These conditional statements are generally of the form `if... then... else`, and often you only see the `if...then`.  Here's the general format for such a statement:
```bash
if [ condition ]; then
  do some stuff;
fi
```
Note that you MUST end the statement with `fi`.  So, in read life this looks like:
```bash
my_number=9
if [ $my_number = 9 ]; then
  echo "my number is 9";
fi
```
Notice a couple of things here, first, be sure to use the `$` in the variable name after declaring the variable.  Second, notice that you MUST include spaces between the square brackets `[]` and the condition being evaluated.  This will not work:
```bash
my_number=9
if [$my_number = 9 ]; then
  echo "my number is 9";
fi
```
Notice that you get an error:
```bash
bash: [9: command not found
```
When trying to run this. SO, you MUST include the spaces between the brackets and the conditition being evaluated.

### else

You can add an `else` clause to these statements, like so:
```bash
my_number=10
if [ $my_number = 9 ]; then
  echo "my number is 9";
else
 echo "my number is something else";
fi
```

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