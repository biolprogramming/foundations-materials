# Lecture 05

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
