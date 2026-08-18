# Lecture 02

For lecture 01, we discussed a little bit about what the command line is and how to go about running a your Codespace on Github.  Refer to the syllabus for the link to the slides used during lecture.  

# In class exercises - command line

The command line is a very powerful tool for working with your computer.  Because it's powerful, there's lots of stuff you can do with it... but it can also be complicated and hard to remember.  One of the most common commands you will use is the `ls` command.

## ls

`ls` stands for "list" and it will show you a list of files that exist in your current directory.  Below, type `ls` into the "terminal" (the place where you type commands) and see what happens.

When you type the command you should see something similar to the following:
```bash
@brantfaircloth ➜ /workspaces/foundations-codespace (main) $ ls
LICENSE  README.md  img  requirements.txt
```
This basically shows the files that exist in what is known as our "working directory".  This is a "directory" or "folder" that is nested within the hierarchy of folders that we discussed.

When you type `ls` it actually runs a program to "list" the directory contents.  The `ls` program, like many Linux and other command line programs, takes what are known as "arguments".  You might also know these as "flags".  These arguments change the behavior of the program you are running.  So, if I type `ls` with an argument, like `ls -l` - the program will output different information.  Try that below, now:
```bash
ls -l
```
And, when you do that, you will see something like the following, which shows some of the same information as above, but is a bit more involved.  Now for each file, there is additional information listed.  That information breaks down into the file permissions, the file owner, the group the file is in, the size of the file, the time it was modified, and it's name.
```bash
-rw-rw-rw-  1 vscode root 1081 Aug 18 18:30 LICENSE
-rw-rw-rw-  1 vscode root  592 Aug 18 18:30 README.md
drwxrwxrwx+ 2 vscode root 4096 Aug 18 18:30 img
-rw-rw-rw-  1 vscode root   80 Aug 18 18:30 requirements.txt
```
File permissions are complicated, and we're not going to spend a lot of time on then.  For every file in linux, there is a "file owner".  "File owners" can also belong to "groups".  Both file owners and groups have "permissions" that specify what they can and cannot do with a file.  Permissions generally come in groups of three, so the above breaks up into:
```bash
- rw- rw- rw-
```
The first dash shows the file type.  If the first item was a directory, that dash would be a "d".  The remaining groups show the permissions for the "owner", the "group" and "everyone".  And the "rw-" means that the owner and the group can "read" (r) and "write" (w) to this file.  The last group of "rw-" means that "everyone" with an account on the computer can read and write to a file.  You can modify permissions to restrict access using the program `chmod`.  We generally will not need to worry about this.

We can actually keep adding more arguments to the `ls` command by stacking them up.  `ls` takes an argument `-h` that outputs the file size in "human readable" format.  So, if we run:
```bash
ls -lh
```
We get the "long directory listing" (`-l`) and we get the file sizes in "human readable" (`-h`) form, like so:
```bash
-rw-rw-rw-  1 vscode root 1.1K Aug 18 18:30 LICENSE
-rw-rw-rw-  1 vscode root  592 Aug 18 18:30 README.md
drwxrwxrwx+ 2 vscode root 4.0K Aug 18 18:30 img
-rw-rw-rw-  1 vscode root   80 Aug 18 18:30 requirements.txt
```

## pwd

In addition to `ls` is the program `pwd`.  `pwd` stands for "present working directory" and when you run it, it shows you your location in the filesystem.  Try to run that now:
```bash
pwd
```
When you do, you should see that it shows something similar to:
```bash
/workspaces/foundations-codespace
```
This is what is known as the "path" to where the files we are looking at are located. Notice, that in the terminal below, the path output by `pwd` is in your header line of the terminal, which is pretty helpful because it shows you where you are located on the filesystem at all times.

## cd

Okay - `ls` and `pwd` show you information about *where* you are located on the filesystem.  Often, we need to move around the file system to change from one directory or another or to help copy a file from one location to another location. `cd` is a program that "changes directories".  You type `cd` followed by a path that you want to go to, and the computer will send you to that location.  Type:
```bash
cd /
```
Where does this take us?  How do we get back to where we just were? Well, we can get back two ways.  First, `cd /` puts us at the "root" of the filesystem (we discussed this).  We want to move back to the directories we were working in.  So, one thing we could do is type:
```bash
cd /workspaces/foundations-codespace
```
And, we're right back where we started.  Now, let me show you a shortcut.  First, go back to the root directory:
```bash
cd /
```
Now, to navigate back to the last place we were located, we can type:
```bash
cd -
```
And this brings us right back.  Try it! Now, `cd` can take arguments that include a path to some location (e.g. like `/workspaces/foundations-codespace`, above).  These are known as "absolute paths"
because they contain every step of the process to get to a location on the operating system.  There are also what are known as "relative paths" and these tend to confuse people.  A relative path consists of a series of dots, so:
```bash
cd ../
```
Means "go UP (closer to root) one directory from where I'm currently located".  Run that now, and see how your location changes:
```bash
cd ../
```
Notice that now, instead of being in `/workspaces/foundations-codespace` we have moved up one level to `/workspaces/`.  We can go back by typing the entire path to where we want to go or by using `cd -`.  Do that now:
```bash
cd -
```
And, notice that we're back in `/workspaces/foundations-codespace`.  Relative paths are pretty handy because if we want to go up TWO levels in the directory hierarchy, we can run:
```bash
cd ../../
```
Do that now, and see where you end up... This should take you up *two levels* to `/`.  Again, we can get back to where we started using `cd -` or by entering the path to the location we want to go:
```bash
cd /workspaces/foundations-codespace
```
You will likely need to navigate around on the command-line at some point, so known how `cd` and relative and absolutely paths work is very helpful.  It will take a little bit of practice to get used to.

## mkdir

Sometimes, we want to create things on the command-line.  One thing we might want to create are "directories", which we do using the `mkdir` (make directory) command. So, in our current location, let's make a directory named `TMP`:
```bash
mkdir TMP
```
Now, let's look to see if we actually made it:
```bash
ls -lh
```
If we look closely at this ouput, we'll see something like:
```bash
-rw-rw-rw-  1 vscode root 1.1K Aug 18 18:30 LICENSE
-rw-rw-rw-  1 vscode root  592 Aug 18 18:30 README.md
drwxrwxrwx+ 2 vscode root 4.0K Aug 18 18:30 img
-rw-rw-rw-  1 vscode root   80 Aug 18 18:30 requirements.txt
drwxrwxrwx+ 2 vscode vscode 4.0K Aug 26 16:38  TMP
```
Which shows the new directory we just created. Notice that it has `rw` permissions, but also `x`, which stands for "execute" and means that the owner, a member of the group, or anyone can enter the `TMP` directory.

Navigate into `TMP`:
```bash
cd TMP
```
Let's see where we are:
```bash
pwd
```
Notice that `pwd` provides the following path:
```bash
/workspaces/foundations-codespace/TMP
```
And it shows that we have navigated to this directory.

## nano

There are different types of command line programs that you can run, and `nano` is a pretty common one.  `nano` is a command-line-based text editor - so you use it for editing (writing) text of different types.  There are several text editors like `nano`, but it is by far the easiest to use. While you are in your new `TMP` directory, let's run nano:
```bash
nano test.txt
```
Here we have told nano to create and start editing a new file named `test.txt`.  You should see the window pop up that shows the file name at the top, `[New File]` at the bottom, and a bunch of key options below that.  First, add whatever text you like to the file by typing it in.  I'm going to enter 1-20 on each line:
```bash
1
2
3
4
5
...
20
```
To save the file, we hit `<ctrl-x>` and choose "Yes" when it asks if we can to "Save modified buffer" (this is a fancy way of asking if we want to save the file).  Now, if you run `ls` you should see this `test.txt` file in our `TMP` directory:
```bash
ls -lh
```
The results should look like:
```bash
-rw-rw-rw- 1 vscode vscode 4.0K Aug 26 16:38 test.txt
```

## cat

`cat` is a command-line program for `concatenating` files.  It can help you do a lot of things, and one of the helpful things is to output the entire contents of a file to the screen.  Run:
```bash
cat test.txt
```
In the directory in which you just created the file.  That should output the file contents all at once:
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
11
12
13
14
15
16
17
18
19
20
```
We'll come back to `cat` later.

## head

Let's say that we don't want to see the entire file all at once, we just want to see the first few lines at the top of the file.  That's where the program `head` comes in.  Let's run `head` on our test file:
```bash
head test.txt
```
Notice that it only outputs the first 10 lines of the file (if your file is longer than 10 lines):
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
We can adjust the number of lines output by passing the `-n` flag and specifying a number of lines:
```bash
head -n 3 test.txt 
```
This gives us:
```bash
1
2
3
```
This may seem trivial, but it's very useful when you are dealing with HUGE files and just want to see whats at the top...

## tail

... or the bottom.  `tail` is similar to `head` but it shows the LAST few lines of a file.  We can run:
```bash
tail -n 3 test.txt
```
And this gives us:
```bash
18
19
20
```

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
