# Foundations of Computing for Biologists (BIOL2601/7800)
## Homework 04

## Assistance
* Instructor: Brant Faircloth (brant@lsu.edu)
* Office Hours:
    * See scheduling link on [Moodle][1]
* Graduate Teaching Assistant: Rujuta Vaidya (rvaidy2@lsu.edu)
* Office Hours:
    * See scheduling link on [Moodle][1]

[1]: https://moodle.lsu.edu

## Useful Links

* [Syllabus](https://github.com/biolprogramming/found-syllabus)
* [Schedule](https://github.com/biolprogramming/foundations-syllabus?tab=readme-ov-file#schedule) (Lecture slides)
* Your github codespace, where you can access additional lecture notes (using `course-get`)

## Getting course materials

From the terminal inside your Codespace:

```
course-get list             # see what's available
course-get lecture 0        # pull lecture 00 into lectures/lecture00/
course-get homework 0       # pull homework 00 into homework/hw00/
```

# Assignment

Remember to follow instructions. See the RUBRIC.md for scoring (and deductions). This includes deductions for not following the rules.

1. (5 pts) In the folder `question1-in` are 100 files named like `file1.txt`, `file2.txt`, etc.  Create a file named `question1.sh`, and in this file write a `bash` script that will **copy** (not move) all of these files to a new directory `question1-out`, while also changing their extension from `.txt` to `.fasta` (so you will have `file1.fasta`, `file2.fasta`).  Be sure to include the shebang as the first line of your answer file. This can be a `for` loop or a `while` loop.

2. (5 pts) Create a file named `question2.sh`. In that file, include the shebang for `bash` as the first line. Then, write a `bash` loop that computes the sum of the numbers from 20 to 50. Your program should `echo` this total to the terminal.  The total is 1085.  You must write a loop to do this (e.g. don't just add something like `echo 1085` to your `question2.sh` and expect to receive credit). This can be a `for` loop or a `while` loop.

3. (5 pts) Create a file named `question.sh`.  In that file include the shebang for `bash` as the first line.  Then, write a `bash` loop that creates a new file called `random-numbers.txt` and writes a set of 50 random numbers to that file. Make sure that the resulting `random-numbers.txt` file actually contains all 50 numbers. This can be a `for` loop or a `while` loop.

4. (10 pts) I expect that you will have to look part of this up... specifically how to get the first letter of a word on a line using `bash`. So, in the file `data/bird-genera.txt` is a list of bird genera from the Clements Taxonomy. You saw this file in the last assignment.  Create a file named `question4.sh`, and in that file, include the shebang for `bash` as the first line.  Then, write `bash` script that loops over `data/bird-genera.txt` and counts all of the bird names that **BEGIN** with an "S".  Your program should `echo` this total to the terminal.  The total is 809.  In addition to using a loop, you will likely have to use conditionals. Your loop can be a `for` loop or a `while` loop.
