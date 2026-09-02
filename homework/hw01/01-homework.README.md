# Foundations of Computing for Biologists (BIOL2601/7800)
## Homework 01

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

All answer files should be uploaded to Moodle. **For this assignment**, you can place all of your answers into **one single file** and you will upload that single file to [Moodle][1] under Assignment 1. Please copy the questions below to a text file, and place your answers below **each specific question**. Some of these questions are similar to the types of questions that you may see on the written exam.

1. (5 pts) `ls` gives directory listings, and we can use additional flags (like `-lh`) to get more information regarding files and directories. What is the output of `ls /bin`? Meaning, what is this command showing (put another way, what type of files live in `/bin`)? You may need (and use) external resources to look some of these up. If you do, explain what you used or where you found your answer.
2. (5 pts) Pick one of the things in `/bin` being listed and look up what that thing does (you might consider a Google search using `<thing name> linux /bin`). You might also investigate how the `man` command works by running (on the command line) `man <thing name>`. Explain what you picked, which method you used to find information about the thing, and what you think the thing it does. Please describe in your own words.
3. (5 pts) In your own words, what is the difference between "storage"  (aka the "hard-drive") in a computer and "RAM" or "memory" in a computer? Which one do you usually get more of when you buy a standard computer? Which one is faster?
4. (5 pts) Use `nano` to create a file in `TMP` (which you may have to create) named `test-numbers.txt` with the following contents:
    ```
    01
    10
    11
    12
    21
    02
    03
    04
    05
    06
    07
    08
    09
    15
    16
    17
    18
    19
    20
    13
    14
    ```
    Now, in the same location where you created the file, run the following command `cat test-numbers.txt | sort`. In your own words, explain what this process is doing.

5. Now, use `nano` to create a second file (also in `TMP`) named `test-numbers2.txt` with the contents below.  Once you have done that, run the following command `cat test-numbers2.txt | sort`. In your own words, explain what this process is doing and how it differs from what you did AND what happened in question 4.
    ```
    1
    10
    11
    12
    21
    2
    3
    4
    5
    6
    7
    8
    9
    15
    16
    17
    18
    19
    20
    13
    14
    ```

**Totally Optional**: If you have a mac or a windows machine (with the linux subsystem installed), see if you can find the command line and run some of the commands we ran today on your own machine.
