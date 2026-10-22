# Foundations of Computing for Biologists (BIOL2601/7800)
## Homework 06

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

Remember to follow instructions. See the [RUBRIC.md](RUBRIC.md) for scoring (and deductions). This includes deductions for not following the rules.

These are all going to be rather easy, as we work out way into programming Python. To make things a little easier for you, here is a little bit of code to get you started.  When you create each file below, you can paste this in to get a correctly formatted template for a working program:
```python
#!/usr/bin/env python


def main():
    pass


if __name__ == "__main__":
    main()
```

1. (5 pts) In a file named `question1.py`, I want you to write a very small program to _**print**_ the name of the person who invented Python using the `print()` function.  You should include the shebang, you should include an `ifmain` statement, and that `ifmain` statement should run a function named `main()` (i,e. paste in the above template to `question1.py`).  Place the `print()` function call that will output the name of the person who invented Python in the `main()` function.

2. (5 pts) Now that you know how to structure your Python programs correctly, I want you always to follow that format (e.g. include shebang, `ifmain`, and a `main()` function).  And, now that you know a little bit about how to print things using the `print()` function, in a file named `question2.py`, I want you to find out what the most famous one-line, first programming exercise is (you've actually done this in class), and write that bit of code for Python (hint: it involves using `print()`).  For examples of what this most famous exercise might be, and what it looks like in other languages (if you are interested), check [here](http://helloworldcollection.de/).

3. (5 pts) Ok, now that you have some practice with the `print()` and you know how to use the `print()` statement to output text (or more appropriately, a _string_), now use the `print()` statement to output the sum of the year Python was invented with the year of Guido van Rossum's birthday.  Place your answer in `question3.py`, be sure to format the program as I've asked (e.g. shebang, `ifmain`, and a `main()` function), and compute and output this sum in the `main()` function.

4. (5 pts) This one is a little trickier.  In `question4.py`, write a correctly structured program (e.g. includes shebang, `ifmain`, and a `main()` function) that prints the numbers 0 to 50 by five as part of the `main()` function.  When you run this program it should output:
    ```
    [0,5,10,15,20,25,30,35,40,45,50]
    ```

5. (5 pts) Finally, in `question5.py`, write a correctly structured program (e.g. includes shebang, `ifmain`, and a `main()` function) using the `print()` function and what's known as "string substitution", to **substitute** the values of two variables into a string.  The two variables should contain the values `October 22` and `6` and you should substitute those variables into a string so that the final output reads:
    ```
    The due date for this assignment is October 22 meaning we have 6 weeks left in this course
    ```
    You may want to have a look at the [string formatting documentation](https://docs.python.org/3/tutorial/inputoutput.html) for Python.
