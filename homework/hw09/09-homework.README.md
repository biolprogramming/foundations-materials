# Foundations of Computing for Biologists (BIOL2601/7800)
## Homework 09

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


1. (5 pts) In the file named `question1.py`, I have created a stub of a program that contains a long string (that is set to a variable called `data`) holding the following data:
    ```
    ExaML_info.T2	Likelihood of best tree:	-82924253.01
    ExaML_info.T0	Likelihood of best tree:	-82924366.59
    ExaML_info.T19	Likelihood of best tree:	-82924465.57
    ExaML_info.T8	Likelihood of best tree:	-82924354.98
    ExaML_info.T16	Likelihood of best tree:	-82924424.87
    ExaML_info.T12	Likelihood of best tree:	-82924426.53
    ExaML_info.T4	Likelihood of best tree:	-82924397.48
    ExaML_info.T10	Likelihood of best tree:	-82925366.65
    ExaML_info.T9	Likelihood of best tree:	-82924194.73
    ExaML_info.T7	Likelihood of best tree:	-82924252.98
    ExaML_info.T11	Likelihood of best tree:	-82925447.60
    ExaML_info.T6	Likelihood of best tree:	-82924194.67
    ExaML_info.T1	Likelihood of best tree:	-82924354.95
    ExaML_info.T17	Likelihood of best tree:	-82924707.69
    ExaML_info.T3	Likelihood of best tree:	-82924424.89
    ExaML_info.T14	Likelihood of best tree:	-82924426.52
    ExaML_info.T18	Likelihood of best tree:	-82925393.89
    ExaML_info.T13	Likelihood of best tree:	-82924426.54
    ExaML_info.T5	Likelihood of best tree:	-82924194.71
    ExaML_info.T15	Likelihood of best tree:	-82924366.58
    ```
    These are log-likelihood values output by the program [RAxML/ExaML](https://github.com/stamatak/standard-RAxML), which is commonly used for [phylogenetic inference](https://en.wikipedia.org/wiki/Phylogenetics). Log-likelihood values are used to rank models of different possible evolutionary histories, and finding the smallest negative log-likelihood value (the one closest to 0) indicates the "best" model.
    
    I want you to write the remaining code to take the value of this string and process these log-likelihood data. Specifically, I want you your program to split the lines by line ending, replace the tab separations with commas, and print out the result.

2. (10 pts) In the file named `question2.py`, I want you to continue the exercise above - process the string stored in the `data` variable to split the lines by line ending, replace the tab separations with commas, and print out the result.  This is the same as `question1.py`.  I would just copy this part of the code over.

    What is **not the same** is that I want you to write additional code to sort each line such that it is eventually written out to the screen so that you "minimize the negative log-likelihood". This means that I want you to print the lines in order from the smallest (closest to zero) to the largest value of the log-likelihood following the same output format as you did in `question1.py`.

3. (10 pts) In the file named `question3.py` is another stub of a program.  This one sets a variable `darwin` equal to the contents of the first two paragraphs of Darwin's ["On the origin of species"](https://www.gutenberg.org/files/1228/1228-h/1228-h.htm#chap01).  That text looks like:
    ```
    When we look to the individuals of the
    same variety or sub-variety of our older
    cultivated plants and animals, one of
    the first points which strikes us, is,
    that they generally differ much more
    from each other, than do the individuals
    of any one species or variety in a state
    of nature. When we reflect on the vast
    diversity of the plants and animals
    which have been cultivated, and which
    have varied during all ages under the
    most different climates and treatment, I
    think we are driven to conclude that
    this greater variability is simply due
    to our domestic productions having been
    raised under conditions of life not so
    uniform as, and somewhat different from,
    those to which the parent-species have
    been exposed under nature. There is,
    also, I think, some probability in the
    view propounded by Andrew Knight, that
    this variability may be partly connected
    with excess of food. It seems pretty
    clear that organic beings must be
    exposed during several generations to
    the new conditions of life to cause any
    appreciable amount of variation; and
    that when the organisation has once
    begun to vary, it generally continues to
    vary for many generations. No case is on
    record of a variable being ceasing to be
    variable under cultivation. Our oldest
    cultivated plants, such as wheat, still
    often yield new varieties: our oldest
    domesticated animals are still capable
    of rapid improvement or modification.
    
    It has been disputed at what period of life
    the causes of variability, whatever they
    may be, generally act; whether during
    the early or late period of development
    of the embryo, or at the instant of
    conception. Geoffroy St. Hilaire’s
    experiments show that unnatural
    treatment of the embryo causes
    monstrosities; and monstrosities cannot
    be separated by any clear line of
    distinction from mere variations. But I
    am strongly inclined to suspect that the
    most frequent cause of variability may
    be attributed to the male and female
    reproductive elements having been
    affected prior to the act of conception.
    Several reasons make me believe in this;
    but the chief one is the remarkable
    effect which confinement or cultivation
    has on the functions of the reproductive
    system; this system appearing to be far
    more susceptible than any other part of
    the organisation, to the action of any
    change in the conditions of life.
    Nothing is more easy than to tame an
    animal, and few things more difficult
    than to get it to breed freely under
    confinement, even in the many cases when
    the male and female unite. How many
    animals there are which will not breed,
    though living long under not very close
    confinement in their native country!
    This is generally attributed to vitiated
    instincts; but how many cultivated
    plants display the utmost vigour, and
    yet rarely or never seed! In some few
    such cases it has been found out that
    very trifling changes, such as a little
    more or less water at some particular
    period of growth, will determine whether
    or not the plant sets a seed. I cannot
    here enter on the copious details which
    I have collected on this curious
    subject; but to show how singular the
    laws are which determine the
    reproduction of animals under
    confinement, I may just mention that
    carnivorous animals, even from the
    tropics, breed in this country pretty
    freely under confinement, with the
    exception of the plantigrades or bear
    family; whereas, carnivorous birds, with
    the rarest exceptions, hardly ever lay
    fertile eggs. Many exotic plants have
    pollen utterly worthless, in the same
    exact condition as in the most sterile
    hybrids. When, on the one hand, we see
    domesticated animals and plants, though
    often weak and sickly, yet breeding
    quite freely under confinement; and
    when, on the other hand, we see
    individuals, though taken young from a
    state of nature, perfectly tamed, long-
    lived, and healthy (of which I could
    give numerous instances), yet having
    their reproductive system so seriously
    affected by unperceived causes as to
    fail in acting, we need not be surprised
    at this system, when it does act under
    confinement, acting not quite regularly,
    and producing offspring not perfectly
    like their parents or variable.
    ```
    I want you to complete the program by writing functions to: (1) remove the punctuation in the two paragraphs of text and (2) count the number of unique words used in both paragraphs (remember to also make everything all upper- or lower-case or your counts will be off).
    
    **You cannot use python's `Counter()` class for this - you  must use what you know about dictionaries, strings, iteration, and counting.**

    You'll also probably also be tempted to ask AI for help on this one, but I wouldn't.  One, you'll learn more figuring it out.  Two, the AI answer might just be wrong.

    I have removed all line endings from the value of the variable `darwin`, so that's one less thing you need to worry about...
