# Lecture 6

## Character escaping

You've already seen this a little bit, but often you need to use character escaping when you are doing stuff on the shell. What does this mean? Basically that you need to differentiate between words and symbols that you are doing something like searching for and words and symbols that mean something to the shell.

For example, `bash` has a number of symbols that it uses that are known as "shell metacharacters" that you need to escape when you use. From the [bash manual](https://www.gnu.org/software/bash/manual/html_node/Definitions.html):
```
A character that, when unquoted, separates words. A metacharacter is a space, tab, newline, or one of the following characters: ‘|’, ‘&’, ‘;’, ‘(’, ‘)’, ‘<’, or ‘>’.
```
So, when you are doing something like a literal search for these characters in a file, you need to escape them.  For instance, let's say we want to search for where I used `>` in `Lecture-4.md`:
```bash
cat Lecture-4.md | grep >
```
Whoops - that doesn't work (you get an error).  But if we escape the character, things work better
```bash
cat Lecture-4.md | grep ">"
```
This is the essence of character escaping. Like many other aspects of `bash`, you can escape characters in several ways - you can use single or double quotes, like above.  You can also use a non-quoted backslash, like so:
```bash
cat Lecture-4.md | grep \>
```
You can also use these character escapes when a filename contains something like a space.  So:
```bash
ls "this is my filename"
```
will work, as will:
```bash
ls "this\ is\ my\ filename"
```
Finally, if the thing you are escaping contains quotes, things can get complicated.  For example, if whatever your want to search for contains a single quote `'`, then you must surround that with double-quotes `"`.

## Variables
`bash` let's you do what's called "declare" variables.  And, once declared, you can use those variables again for different tasks.  You declare a variable in `bash` like so... let's say that we want to make this variable equal to the path `/workspaces/foundations-2024-lectures-found-class-template/examples`, we can do that by:
```bash
MY_DIR=/workspaces/foundations-2024-lectures-found-class-template/examples
```
If you paste that into the terminal and hit enter, nothing really happens.  However, if you `cd` to this directory:
```bash
cd $MY_DIR
```
You'll actually change directories to the one we set equal to the variable. NOTICE that **TO USE** a variable, we must precede that variable name with a `$` sign.  Typically, `bash` variables are capitalized, although that is just a convention.

There are also some pre-set variable in `bash`.  One of those is `$RANDOM`.  Every time you call that, you get a new random number drawn from the built-in random number generator that is part of the operating system (random numbers are used a lot in operating systems):
```bash
echo $RANDOM
echo $RANDOM
echo $RANDOM
```

Another of those built-in variables is known as `$PATH`.  This specifies which programs you can run without specifying their full path (to the program name):
```bash
echo $PATH
```
You'll see something like:
```bash
/usr/local/rvm/gems/ruby-3.3.4/bin:/usr/local/rvm/gems/ruby-3.3.4@global/bin:/usr/local/rvm/rubies/ruby-3.3.4/bin:/vscode/bin/linux-x64/38c31bc77e0dd6ae88a4e9cc93428cc27a56ba40/bin/remote-cli:/home/codespace/.local/bin:/home/codespace/.dotnet:/home/codespace/nvm/current/bin:/home/codespace/.php/current/bin:/home/codespace/.python/current/bin:/home/codespace/java/current/bin:/home/codespace/.ruby/current/bin:/home/codespace/.local/bin:/usr/local/python/current/bin:/usr/local/py-utils/bin:/usr/local/oryx:/usr/local/go/bin:/go/bin:/usr/local/sdkman/bin:/usr/local/sdkman/candidates/java/current/bin:/usr/local/sdkman/candidates/gradle/current/bin:/usr/local/sdkman/candidates/maven/current/bin:/usr/local/sdkman/candidates/ant/current/bin:/usr/local/rvm/gems/default/bin:/usr/local/rvm/gems/default@global/bin:/usr/local/rvm/rubies/default/bin:/usr/local/share/rbenv/bin:/usr/local/php/current/bin:/opt/conda/bin:/usr/local/nvs:/usr/local/share/nvm/versions/node/v20.16.0/bin:/usr/local/hugo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/share/dotnet:/home/codespace/.dotnet/tools:/usr/local/rvm/bin
```
So, the operating system checks all of these locations when you type a program name for that program.  Remember that if you type `which` it tells you where a program is located:
```bash
which pwd
```
So, the path to this program is `/usr/bin/pwd`, but you only have to type `pwd` because `/usr/bin/` is already in your `$PATH`.  Updating your `$PATH` is something that you sometimes have to do - we won't cover it for this class, but you can look at details online.

### Variables can use other variables

If you specify one variable, you can use that to create another.  E.g. if you have a variable `MY_PROGRAM`:
```bash
MY_PROGRAM=some_name_here
```
You can combine that with another variable named `MY_PTH` which has the value of `/path/to/` like so:
```bash
MY_PTH=/path/to
```
Now, take a look at:
```bash
echo $MY_PTH/$MY_PROGRAM
```
You can even set these to a third variable if you like:
```bash
MY_FULL_PTH=$MY_PTH/$MY_PROGRAM
echo $MY_FULL_PTH
```

## Variables and curly braces {}

Lots of times, you'll see variables surrounded by curly braces, particularly when the variable is used in a string ("text like this").  The rules for this are summed up pretty nicely in [this stackoverflow post](https://stackoverflow.com/questions/8748831/when-do-we-need-curly-braces-around-shell-variables):


> Variables are declared and assigned without `$` and without `{}`. You have to use
> ```bash
> var=10
> ```
> to assign. In order to read from the variable (in other words, expand the variable), you must use $.
> ```bash
> $var      # use the variable
> ${var}    # same as above
> ${var}bar # expand var, and append "bar" too
> $varbar   # same as ${varbar}, i.e expand a variable called varbar, if it exists.
> ```

So, if you have some variable:
```bash
fname=file
```
And you want to add an extension:
```bash
echo "${fname}.txt"
```
But also note that simply using:
```bash
echo "$fname.txt"
```
Will sometimes work, so the squiggly braces can be inconsistent.

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

## Looping

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

### Doing some math in a loop

Let's write some code to get the number 1..10 but sum them up as we go.  You have to be a little creative about this:
```bash
result=0
for i in {1..10}; do
  a=$i;
  result=$(($result+$a));
done
echo $result
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
