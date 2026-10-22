# Foundations of Computing for Biologists (BIOL2601/7800)
## Homework 07

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

Remember to follow instructions. See the [RUBRIC.md](RUBRIC.md) for scoring (and deductions). This includes deductions for not following the rules. To make things a little easier for you, here is a little bit of starter code to get you going.  When you create each file below, you can paste this in to get a correctly formatted template for a working program:
```python
#!/usr/bin/env python


def main():
    pass


if __name__ == "__main__":
    main()
```

1. (5 pts) This is a modification of Question 4 from your previous assignment. In a file named `question1.py`, I want you to write a correctly structured program (e.g. includes shebang, `ifmain`, and a `main()` function) that takes input from the user consisting of some maximum integer value. Then, I want you to pass that maximum value to a function (e.g. as an argument) in your program named `to_fifty()` (meaning, the function name should be `to_fifty()`).  That function will consist of code that will compute and print (to the screen) values from 0 to the maximum value entered by the user **in increments of 5** (inclusive of the maximum value, if it is divisible by 5).  For example, if I enter 25, this should print:
    ```
    [0, 5, 10, 15, 20, 25]
    ```
    If I enter 45, this should print:
    ```
    [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
    ```
    If I enter 24, this should print:
    ```
    [0, 5, 10, 15, 20]
    ```

2. (5 pts) In a file named `question2.py`, modify the function(s) you wrote for Question 1 so that the `to_fifty()` function returns the list from 0 to <maximum integer> by 5 **IN REVERSE** and outputs that to the screen. For example, if I enter 25, this should print:
    ```
    [25, 20, 15, 10, 5, 0]
    ```

3. (15 pts) _e_  is a mathematical constant that is sometimes known as [Euler's number](https://en.wikipedia.org/wiki/Leonhard_Euler) number. For the history of e, see [Wikpedia](https://en.wikipedia.org/wiki/E_(mathematical_constant)). The value of  e is **approximately**  `2.71828`, and the reason the value of e is approximate is that it can be computed as:

    $e=\sum_{n=0}^{\infty} \frac{1}{n!} =  1 + \frac{1}{1} + \frac{1}{1\cdot2} + \frac{1}{1\cdot2\cdot3} + ...$

    So, now the tricky part.  In `question3.py`, write a program that uses functions to calculate _e_ .  Because _e_  is computed as the limit approaches infinity, you should limit the upper range of values you input to the function to <=1,000.  Set the program up so that a `main()` loop calls the function computing _e_, and this function returns the approximate value of _e_ to the `main()` loop, which then prints the value of _e_ that you have computed to the screen.

    You may not use `math.e` in any way (e.g. you **MUST** compute _e_).

    You do not need to use recursion, although you can if you would like to confused yourself.
