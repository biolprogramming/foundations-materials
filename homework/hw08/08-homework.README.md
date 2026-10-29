# Foundations of Computing for Biologists (BIOL2601/7800)
## Homework 08

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

1. (5 pts) You're going to finish writing part of a program that uses conditionals to deal with text.  In this instance, in `question1.py`, I've written the `main()` function for you.  You need to fill out the `check_text()` function.  I want you to write a function body for `check_text()` that checks if each sentence is uppercase, lowercase, or titlecase, I want the function to print which one it is, and I then want the function to titlecase each sentence passed to it and print the titlecased version out.

2. (5 pts) Similar to the above, I want you to finish writing the palindrome checker program that I've started in `question2.py`.  The main function should take input from the user, then pass that input to the `check_palindrome()` function, check the text to see if it is a palindrome, then return `True` or `False` to the `is_palindrome` variable in the main loop, which will print whether or not the phrase input by the user was (or was not) a palindrome.

3. (5 pts) We talked about iteration and using `while` and `for` to accomplish iteration.  For `question3.py`, I want you to build off the new knowledge you have of `while` and `for` loops while revisiting a couple of tasks that you've already seen.  In `question2`, we talked about palindromes.  They're fun to think about and I like them, so in `question3.py` I want you to complete the body of the `output_palindrome` function to take the arguments being passed from `main()` and print that output from the `output_palindrome` function, word-by-word, so that the output looks like the following. You **MUST** use a `while` or a `for` loop:
    ```
    able
    was
    i
    ere
    i
    saw
    elba
    ```

4. (10 pts) Prime numbers are important in a lot of industries, particularly cryptography.  The definition of a prime number is an integer value ("natural number") greater than one that can only be divided by 1 and itself (or, put another way, the prime number cannot be formed by multiplying two, smaller, natural numbers).  In `question4.py`, write a program that uses for loop(s) to compute the prime numbers found between 0 and 100. Write those numbers out to the screen in a format that looks like:
    ```
    2
    3
    5
    7
    ...
    97
    ```
    Be sure to use the `main()` function to call whatever you name your "prime checking" function and pass this prime checking function variables for the minimum and maximum values across which to compute the primes (0 to 100 in this case). 

    You can print the prime numbers to the screen from this "prime checking" function (whatever you call it) if you would like (or you can do it from `main()`). You **MUST** use a `for` loop to accomplish this task.