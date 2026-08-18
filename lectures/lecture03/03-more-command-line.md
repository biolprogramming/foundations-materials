# Lecture 03

We previously talked about some basic shell/terminal/command-line interface commands.  We're going to continue down this path by adding some commands that do more useful things.  First, a reminder of how to get help.

## Getting help - `--help` and `man`

You might be wondering how you magically know what flags and options a given program takes on the command line.  There are several ways to get help.  First, some programs will let you used something like:
```bash
head --help
```
And it will show you a brief help screen.  Also note that some programs allow you to use `-h` to accomplish the same thing.  Others do not.  What does `head` do?  You can also get help on various programs by running `man` followed by the program name.  This brings up the "manual" page for the program that you are running.  Try it!
```bash
man head
```
This shows you what is known as the "manual" page for the `head` program and explains how to use it, what it's options are, etc.  Most command line tools on linux have a manual page that will provide you with help if you need it. You scroll through manual pages using the spacebar/arrow keys/page up/page down.  You QUIT by hitting `q`.

## Copying files

Copying files on the command line is pretty easy and uses the `cp` command to "copy".  Basically, if you have a file in one place named `file-i-want-to-copy.txt`, you copy it using the path that you want to move it to.  So if you and `file-i-want-to-copy.txt` are in the came directory and you want to copy that file elsewhere:
```bash
cp `file-i-want-to-copy.txt` /path/to/some/other/directory/
```
This will create a new copy of the file at `file-i-want-to-copy.txt` /path/to/some/other/directory/`. If you want to copy the file AND rename it:
```bash
cp `file-i-want-to-copy.txt` /path/to/some/other/directory/new-name-for-file-i-want-to-copy.txt
```

## Moving files

Moving files is also pretty easy and uses the `mv` command to "move" files. Basically, if you have a file in one place named `file-i-want-to-move.txt`, you move it using the path you want to move it to. So if you and `file-i-want-to-move.txt` are in the came directory and you want to move that file elsewhere:
```bash
mv `file-i-want-to-copy.txt` /path/to/some/other/directory/
```
This will MOVE the `file-i-want-to-copy.txt` to /path/to/some/other/directory/`. If you want to MOVE and rename:
```bash
mv `file-i-want-to-copy.txt` /path/to/some/other/directory/new-name-for-file-i-want-to-move.txt
```

## Pipes (where things start getting interesting)

pipes are an interesting thing on unix-like operating systems that allow you to send the contents of one command to another command so that the second command can do something to the output of the first command.  A pipe is `|` character, and it can be in different places on different keyboards - so you have to find where it is on your keyboard.

We can use a pipe in something like the following scenario, which also uses a program called `sort` (which, you guessed it, sorts stuff).  If you made a list of numbers in `test.txt` then let's reverse that quickly and easily using:
```bash
cat test.txt | sort -r
```
This is telling `cat` to output the contents of the file, pass those contents to `sort` and `sort` is then sorting the results in `-r` or "reverse" order.  When you run that, though, the output looks weird, like so:
```bash
9
8
7
6
5
4
3
20
2
19
18
17
16
15
14
13
12
11
10
1
```
And you'll notice that this is not actually sorted in the reverse order we expected.  Basically, what's happened here is that `sort` has used "string" sorting and not "numeric" sorting to sort the list.  Basically, we need to tell sort that these are numbers we want to sort, which we do using the `-n` flag.  So, we can run:
```bash
cat test.txt | sort -rn
```
And we get:
```bash
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
```
Chaining these commands together can be really, really useful.  I'll give you an example - have you ever had to make a list of unique values from a list that contains repeated values?  Let's do that easily.  First, open up `nano`, and add the following to a file we'll call `make-unique.txt`:
```bash
apples
oranges
apples
oranges
pears
raisins
grapes
grapes
apples
pears
```
To make this list unique, we need to output it through `cat`, sort it using `sort`, then use a final program `uniq` to get the uniq list.  We can chain all of those together using pipes:
```bash
cat make-unique.txt | sort | uniq
```
That should remove duplicates and give us:
```bash
apples
grapes
oranges
pears
raisins
```
We can go one better and actually get a count of the unique things on the command-line, too - we have to add the `-c` option to `uniq` to give us a "count" of each unique item:
```bash
cat make-unique.txt | sort | uniq -c
```

### Finding words in a file

We can also use pipes to do things like find a word or words in a file.  Here, we combine `cat` with a program like `grep`.  `grep` is a powerful program for searching for text using regular expressions (we'll talk about these later).  We can also just use it to find occurrences of words like so:
```bash
cat make-unique.txt | grep apples
```
Notice that this finds three occurrences of "apples".  If we want to get a count of these occurrences, we can go one step further and add in another program called `wc` that, when given the `-l` option to count lines, will count each line on which a word is found by grep:
```bash
cat make-unique.txt | grep apples | wc -l
```
This should output 3.  Somewhat similarly, we can do things like get a count of ALL lines in our `test.txt` file using `wc -l`:
```bash
cat test.txt | wc -l
```
Alternatively, we can also just use `wc -l` directly on the file:
```bash
wc -l test.txt
```

## Shell redirect

One thing that you sometimes encounter when working on the command line is the "redirect" operator - it looks like `>` or `<` which basically translates to "send something out to a place" (`>`) or "read something in from a place" (`<`).  To give you an example of how this works, lets filter our list of fruits and output ONLY those fruits that are `apples` to a new file:
```bash
cat make-unique.txt | grep apples > my_new_file.txt
```
Now, take a look at the contents of this new file using something like `cat`:
```bash
cat my_new_file.txt
```
What do you think happens if we try something like:
```bash
cat test.txt > my_new_file.txt
```
You should see that the contents of `test.txt` completely overwrote the contents of my_new_file.txt.  That might not be what you want to have happen.  If you want to add the new contents to the end of whatever file, you need to use two `>>`, like so:
```bash
# recreate the file
cat make-unique.txt | grep apples > my_new_file.txt

# now, combine the two files:
cat test.txt >> my_new_file.txt
```
Take a look at the resulting output file with `cat`.

### A little more on redirects

Redirects can sort of behave a little bit like `cat` does.  Try this:
```bash
grep apples < make-unique.txt
```
This will print:
```bash
apples
apples
apples
```
to the screen - effectively behaving like `cat` did.  In this case, we've used the redirect to send the contents of `make-unique.txt` **in** to `grep` versus using `cat` to do that.  We can use a redirect in AND out - what do you think:
```bash
grep apples < make-unique.txt > redirect-test.txt
```
will contain?

## less

Speaking of taking a look *into* files, sometimes you want to look in a file that is pretty large, and running `cat` would output the entire thing to the terminal... and you don't want that (e.g. imagine the file is 200-300 GB in size!).  You can use program named `less` to peer into a file on a page-by-page basis.  Let's use that to look at `my_new_file.txt`:
```bash
less my_new_file.txt
```
There are not a lot of lines here to deal with, so we just see the three lines in the file.  If there were lots of lines we could scroll down with the spacebar, and up and down with the arrow keys or page-up/page-down.  

You can see other `less` commands by typing "H" or "h".  You can enter search in `less` by typing `/` followed by whatever you want to search for.

To exit `less`, type `q`.

## rm

So, you've created files, how to do remove them?  That's where `rm` comes in - it "removes" files and directories.  Let's remove the `redirect-test.txt` file from above:
```bash
rm redirect-test.txt
```
That file is now gone FOREVER.  So, be really careful with `rm`.  To delete a directory, we need to use the `-r` flag:
```bash
rm -r some-directory-name
```
This will also get rid of what you delete FOREVER, so be careful.  It's always good to type once, read twice, and THEN hit enter when using `rm`.

## wget

When working on the command-line, you sometimes need to download files from somewhere to wherever you are working.  This can be pretty hard without a graphical interface, and that's where `wget` comes in. Although there are several programs that can get files from the internet, `wget` is one of the easiest to use.  Let's say we want to download a file from the Syllabus repository for this class.  First, we need to find the link to that file (usually, on another computer, go to the file online, right-click, and select "Copy link").  With the link copied, we can download the file like so:
```bash
wget https://raw.githubusercontent.com/biolprogramming/found-syllabus/main/LICENSE
```
This will download the `LICENSE` file from the listed URL to our working directory.  Do it now.  Notice that we already HAD a LICENSE file, so `wget` has named the new file LICENSE.1.  Let's delete that file:
```bash
rm LICENSE.1
```
Now, let's download the same file and give it whatever name we like (notice that this is `-O` (capital O for "Output")):
```bash
wget -O name-that-I-like.txt https://raw.githubusercontent.com/biolprogramming/found-syllabus/main/LICENSE
```
You can use `less` to take a look at that file.  Then go ahead and delete it:
```bash
rm name-that-I-like.txt
```

## history

As I mentioned the other day, the computer keeps track of commands you've typed - and you can adjust how many commands it keeps (my computers are set to keep everything).  You can access these commands using the `history` program like so:
```bash
history
```
Notice that this outputs your history, with a # in the order issued.  Usually, you want to search for something specific, so you use:
```bash
history | grep <whatever command>
```
To extract those history lines that contain whatever you were/are searching for.


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
