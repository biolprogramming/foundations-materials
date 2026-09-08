# Lecture 04

We're continuing on with our tour of different command-line programs today.  Towards the end of the lecture, we should start talking about variables and loops.

## history

As I mentioned the other day, the computer keeps track of commands you've typed - and you can adjust how many commands it keeps (my computers are set to keep everything).  You can access these commands using the `history` program like so:
```bash
history
```
Notice that this outputs your history, with a # in the order issued.  Usually, you want to search for something specific, so you use:
```bash
history | grep <whatever command>
```
To extract those history lines that contain whatever you were/are searching for.  Finally, the `history` command usually outputs a truncated history (e.g. limited to the last 1000 commands or so).  You can access the entire history by appending a `1` to the `history` command like so:
```bash
history 1 | grep <whatever command>
```

## tree

Sometimes, you want a little better picture of the "directory tree" or directory structure of some location on the filesystem, and that's what `tree` is for.  We can run `tree` in our current directory:
```bash
tree ./
```
and that output should look something like:
```bash
./
├── LICENSE
├── Lecture-00
│   └── Lecture-01.md
├── Lecture-01
│   └── Lecture-02.md
├── Lecture-02
│   └── Lecture-03.md
├── Lecture-03
│   └── Lecture-04.md
├── Lecture-04
│   ├── Lecture-05.md
│   └── files
│       ├── file-1.mp3
│       ├── file-1.txt
│       ├── file-10.mp3
│       ├── file-10.txt
│       ├── file-11.txt
│       ├── file-12.txt
│       ├── file-13.txt
│       ├── file-14.txt
│       ├── file-15.txt
│       ├── file-16.txt
│       ├── file-17.txt
│       ├── file-18.txt
│       ├── file-19.txt
│       ├── file-2.mp3
│       ├── file-2.txt
│       ├── file-20.txt
│       ├── file-3.mp3
│       ├── file-3.txt
│       ├── file-4.mp3
│       ├── file-4.txt
│       ├── file-5.mp3
│       ├── file-5.txt
│       ├── file-6.mp3
│       ├── file-6.txt
│       ├── file-7.mp3
│       ├── file-7.txt
│       ├── file-8.mp3
│       ├── file-8.txt
│       ├── file-9.mp3
│       └── file-9.txt
└── README.md
```
You can play around with this in different locations.  `tree` also takes other arguments like:
```bash
tree -h
```
which shows file sizes in "human" readable form along with the size of files in the directory.  And, you can limit the depth to which `tree` displays using the `-L` argument:
```bash
tree -L 1 ./
```
now displays:
```bash
./
├── LICENSE
├── Lecture-01
├── Lecture-02
├── Lecture-03
├── Lecture-04
├── Lecture-05
└── README.md
```

## du

Speaking of file sizes, sometimes you want to know the size of an entire file or directory, and that's where `du` comes in.  It shows "disk usage" of a directory, file, etc.  Let's run it on the current directory - with the human readable option:
```bash
du -h Lecture-05/files/file-2.mp3
```
That should show:
```bash
0B	Lecture-05/files/file-2.mp3
```
So, there's a file there, but it does not contain anything.

## date

The date command does just what it sounds like - it gives you the date and time.  There are lots of options to format its output this or that way:
```bash
date
```
looks like:
```bash
Tue Sep  3 19:19:49 UTC 2024
```
In terms of formatting, we can do stuff like get the time in our own time zone like so:
```bash
TZ='America/Chicago' date
```
This actually uses a variable, which we haven't used yet and will talk about later. `date` is pretty powerful - check out its `man` page for more info.

## touch

Sometimes you just need to create an empty file - that's where `touch` comes in.  It makes totally empty files:
```bash
touch temp-file.txt
```
now take a look:
```bash
ls -lh
```
this should output:
```bash
-rw-rw-rw- 1 codespace codespace    0 Sep  3 19:22 temp-file.txt
```
Also notice that when you `touch` an existing file, it updates its modified time to the current date and time.  It does not actually modify the file.

Let's remove that temp file:
```bash
rm temp-file.txt
```

## which

Sometimes, it's not clear where a program you are running is located, and `which` can help you find that:
```bash
which pwd
```
should display:
```bash
/usr/bin/pwd
```
So this is the `pwd` that is installed a `/usr/bin` (a typical installation location for these programs).

## echo

`echo` can do a lot of stuff... and some of it seems kind of stupid right now but will become useful later.  First, let's use `echo` just to write something to the screen:
```bash
echo "HELLO!"
```
Ok - cool, this printed "HELLO!" to the screen.  Not that exciting.  Let's write "HELLO!" to a file:
```bash
echo "HELLO!" > my-hello-file.txt
```
Now take a look at that file's contents:
```bash
cat my-hello-file.txt
```
Let's remove that file.  We'll come back to `echo` later.
```bash
rm my-hello-file.txt
```

## &&

The `&&` operator is kind of a neat one, it basically means `<do this> AND then <do that>`.  So, you can use it to string together two commands in a row.  This is different from a pipe because the stuff comign out of the first command is not being directed into the second.  For example, I can run:
```bash
ls && ls
```
And this just runs `ls` twice.  That's not very interesting.  But I can run something like this:
```bash
echo "HELLO" && echo " " && echo "THERE!"
```
And that outputs:
```bash
HELLO
 
THERE!
```
Usually, you use `&&` when you want to run one command just after another and you don't want/need to wait to enter the second command.

## aliases

Sometimes, you get tired of typing the same command all the time and you want to type less stuff to get the same thing to happen.  For example, you've been typing:
```bash
ls -alh
```
and most of the options here, you've already seen.  The `-a` option shows so-called "invisible" files.  Typing this all the time is a pain, so we can alias it to another command by typing:
```bash
alias qq="ls -alh"
```
now, instead of typing `ls -alh` all the time, we can type `qq` (in this case, only a little bit shorter).

## ssh

We're not going to use it in this class, but `ssh` is a program for running that is know as a "secure shell".  This means that you can use it to connect to other computers around the globe, and interact with them on the command line.  To connect, you usually run something like:
```bash
ssh <user>@mike.hpc.lsu.edu
```
Then, it will ask you for a password, you enter that password, and then you can do stuff on that remote computer, using the commands we've learned, above.

## wildcards

Wildcards aren't really a program, per se, but they are a way of interacting with the computer on the terminal that can be pretty useful.  Let me give you an example.  I have created a directory named `examples` that will sometimes contain example files.  There is a directory nested within these `examples/lecture-5/files/` that contains 20 files that I created.  We can use these files to understand the idea of wildcards.

Let's say we want to use `ls` to show all files that start with the letter `f`.  We can run:
```bash
ls -al Lecture-05/files/f*
```
This will list every file that starts with an "f". We can also list all files that contain "2" somewhere in their name:
```bash
ls -al Lecture-05/files/file-*2*
```
We can also list only the `txt` files:
```bash
ls -al Lecture-05/files/*.txt
```
Or only the `mp3` files:
```bash
ls -al Lecture-05/files/*.mp3
```
We can even use wildcards on directory names:
```bash
ls -al Lecture-05/f*/*.mp3
```
So, the wildcard operator `*` is just that - a wildcard for something that comes before/after a letter or symbol.  Although we're using `ls` here, you can use wildcards with lots of different commands like `cp`, `mv`, `rm`, etc.

# BASH Programming: Variables, Expressions, Loops

Ok, so many of the commands you've been running above are basically programs that exist in Unix/Linux. However, we've also been working in the "shell" on the command-line... and the shell, itself, can behave like a programming language. There are several of these shell programming languages - `BASH` or `bash` (the Bourne Again SHell) is one of them.  Others are `csh`, `zsh`, `ash`, etc. `bash` is almost always installed as the default shell on most computers you will work with (e.g. it's the default on our HPC).  Many people use `zsh` which is pretty much just like `bash`, but with some additional and really useful bells and whistles.

So, we're going to spend some time talking about how you can basically "program the shell".  This is actually super powerful, because it enables you to do a lot of things very quickly.  But first, a quick note about escaping characters.

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
