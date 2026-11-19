# Foundations of Computing for Biologists (BIOL2601/7800)
## Homework 10 - Bonus

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

1. (10 pts) This is a problem that is similar to something you've done before, but builds upon that knowledge.  In the `data` directory of this this repository, there is a text file named `how-stars-age.txt` that contains a text description of [How Stars Age](http://bit.ly/1TyWglh), written using the 1000 most common words (e.g. the [Up-Goer Five](http://splasho.com/upgoer5/) Challenge).

    In a file named `question1.py`, I want you to write a correctly structured program (e.g. w/ shebang, a main function, and an `ifmain` statement) to count word usage in the text file by **reading in the file from its current location** and counting the words used.  After you count the words, I want you to have this program print out, in decreasing order (most common to least common) the 15 most common words and the count of each of those words.  This should be printed as tab-delimited output to the command line so that the result looks something like what is below.
    ```
    the		16
    it		10
    will		10
    burn		7
    a		7
    very		7
    that		7
    and		7
    air		6
    heavier		6
    ```
      **You MUST write this result out to the command line using f-string formatting**.  You must write your code so that it reads the `how-stars-age.txt` from the `data` directory. You may use any type of tool/module that is part of the Python standard library to accomplish the remaining parts of this task.


2. (15 pts) In the `data` directory are two files:  `darwin-chapter-1.txt` and `darwin-chapter-2.txt` . These are two chapters of Darwin's ["On the origin of species"](https://www.gutenberg.org/files/1228/1228-h/1228-h.htm#chap01). In `question2.py`, write a program that uses `glob` to open and read these chapters as well as some additional code to get a list of all words in each chapter.  Then using f-strings, output to the command line a pretty-printed list of the following:
    - the total count of words in Chapter 1
    - the total count of words in Chapter 2
    - the count of unique words in Chapter 1
    - the count of unique words in Chapter 2
    - the count of words in Chapter 1 that ARE in Chapter 2
    - the count of words in Chapter 1 that ARE NOT in Chapter 2
    - the count of words in Chapter 2 that ARE NOT in Chapter 1
    
    Your program should be properly formatted (e.g. w/ shebang, a main function, and an `ifmain` statement), it should use `glob` to read the two files from the `data` directory, and the output written to the screen should look something like:
    ```
    Total word count
        Chapter 1 = 11615
        Chapter 2 = 4837
    Unique word count
        Chapter 1 = 1991
        Chapter 2 = 1025
    Words in Chapter 1 and Chapter 2:		623
    Words in Chapter 1 not in Chapter 2:		1368
    Words in Chapter 2 not in Chapter 1:		402
    ```
