# Foundations of Computing for Biologists (BIOL2601/7800)
## Homework 03

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

Remember to **follow instructions**. See the RUBRIC.md for scoring (and deductions). This includes deductions for not following the rules. All files should be created with a text-editor (e.g. VS-code on your codespace) and uploaded to [Moodle][1].

1. (6 pts) In the file `data/bird-taxa.txt` is a list of bird species from the Clements Taxonomy (one of the guides for bird names).  In a text file named `question1.sh`, I want you to write a shell command(s) (**including the shebang** that you learned about in the last assignment) that reads this file and provides the correct count of the **number of bird species**. Be sure that the text you place into `question1.sh` contains the code that needs to be run to **produce** the answer. The answer should just display on the terminal (e.g. do not place the answer in a file).

1. (6 pts) In the file `data/bird-genera.txt` is the same list of bird species, but only their genus is shown.  In a text file named `question2.sh`, I want you to write a shell command(s) (**including the shebang**) that shows the (single) bird genus having the highest number of species. Be sure that the text you place into `question2.sh` contains the code that needs to be run to **produce** the answer.  You will need combine several commands together to answer this question.  **The text that is output (to the terminal) should only be one line long** (and that line should show the count and the name of the most numerous genus). Do not place the answer in a file.

1. (6 pts) Using the same data file (`data/bird-genera.txt`), I want you to write a shell command(s) that shows how many times the bird genus _Columba_ appears (birds in the genus _Columba_ are medium to large pigeons).  You should place the shell command that you use to produce the answer into a text file named `question3.sh`.  **Include the shebang**. You will need to combine several commands together to answer this question.  **The text that is output (to the terminal) should only be one line long** (and that line should show how many times _Columba_ appears).

1. (7 pts) In the file `data/bird-species-status.txt` is a list of bird species (in the first column) and a list of extinction status that is coded 0 (not extinct) or 1 (extinct) in the second column.  Using what you know from class, write a shell command that prints the count of extinct bird species to the command line. You should place the shell command that you use to produce the answer into a file named `question4.sh`.  **Include the shebang**. **The text that is output (to the terminal) should only be one line long and display the count of extinct bird species**.
