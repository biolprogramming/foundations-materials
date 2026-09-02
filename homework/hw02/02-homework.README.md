# Foundations of Computing for Biologists (BIOL2601/7800)
## Homework 02

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

## Assignment

Remember to **follow instructions**.  See the [RUBRIC.md](RUBRIC.md) for scoring (and deductions).  This includes deductions for not following the instructions.

All answer files should be uploaded to Moodle. Be sure to create the file(s) as requested and upload those files to [Moodle][1] for the correct assignment.

1. (5 pts) In the file `data/question1.txt` there are 1000 words drawn randomly from a set of 15.  In a file named `question1.sh`, I want you to write a shell command that will:
    1. read/output the contents of this file.
    2. sort those contents in alphabetical order (A-Z).
    3. output the sorted contents **to the terminal**.

    Be sure to create your answer in `question1.sh` so that it reads from the file in `data/question1.txt` (e.g. using that path).

2. (5 pts) Now, in a separate file named `question2.sh`, I want you to write a shell command that will:
    1. read/output the contents of `data/question1.txt`
    2. get the count of unique elements in the file
    3. output the count of unique elements and the element names to a new file `question2-result.txt`

    Be sure to create your answer in `question2.sh` so that it reads from the file in `data/question1.txt` (e.g. using that path).

3. (5 pts) Typically, what you are doing in the 2 problems above (e.g. creating files that run code) is known as writing a "BASH script".  This is because "BASH" is the terminal language we are using, and a "script" is just some code you are running.  BASH scripts should start with a line known as a "shebang". That line looks like `#!/bin/bash`.  It tells the computer that the lines of code that follow are to be run using "BASH" (or some other terminal shell you might be running).  

    Create a new file, `question3.sh` that contains the contents of `question2.sh` but that includes the "shebang" as the very first line. You can do this whatever way to want - copy the file and modify, manually create a new file and paste into it, etc.

4. (5 pts) In a new file named `question4.sh`, include the shebang as the first line and then write a command (or commands) that will combine the data in `data/question4-part1.txt` with the data in `data/question4-part2.txt` and output the contents of both files to a new file named `question4-result.txt`.  See if you can figure out how to add a space between the verses (Hint: you need to include a line-ending between the two).

    Be sure to create your answer in `question4.sh` so that it reads from the files in `data/question4-part1.txt` and `data/question4-part2.txt` (e.g. using those paths).

5. (5 pts) In a new file named `question5.sh`, include the shebang as the first line and then write a command (or commands) that will:
    1. create a new directory named `my-answers`
    2. **copy** each of `question1.sh, question2.sh, question3.sh, question4.sh` to this directory

    Be sure that your answer file (`question5.sh`) is created in **the current directory**.

6. It's optional, but if you found all of these easy (or if you didn't but you like to figure stuff out), head on over to https://cmdchallenge.com for some additional challenges. These get hard.  There are also lots of other places to practice like https://exercism.org/tracks/bash, and there are even entire games based on learning/using BASH skills like [bashcrawl](https://gitlab.com/slackermedia/bashcrawl).
