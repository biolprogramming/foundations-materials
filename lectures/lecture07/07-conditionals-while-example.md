# Lecture 07

## if, elif, else

You can also add a third category of conditions in the form of `elif`, which is read "else if".  These are conditions that fall between the `if` and `then`, and you can have as many as you like of these:
```bash
my_number=2
if [ $my_number = 1 ]; then
  echo "my number is 1";
elif [ $my_number = 2 ]; then
  echo "my number is 2";
elif [ $my_number = 2 ]; then
  echo "my number is 3";
else
  echo "my number is 4";
fi
```
Notice that this evaluates each of the conditions, in turn, until it reaches a satisfactory conclusion.  That said, check this out:
```bash
my_number=10
if [ $my_number = 1 ]; then
  echo "my number is 1";
elif [ $my_number = 2 ]; then
  echo "my number is 2";
elif [ $my_number = 2 ]; then
  echo "my number is 3";
else
  echo "my number is 4";
fi
```
Is that correct?

## Checking for > and <

In `bash`, checks for equality use `=`, as you've seen above.  However, you often test for things like `>`, `<`, `>=`, and `<=`, and there are an entire family of text shortcuts for these (also so you don't have to worry about escaping them).  You can read about all of these in the [advanced scripting guide for bash](https://tldp.org/LDP/abs/html/comparison-ops.html), but the important ones are: `-eq, -ge, -gt, -le, -lt`, which stand for "equality", "greater than or equal", "greater than", "less than or equal", and "less than".  They work mostly like you would expect:
```bash
my_number=10
if [ $my_number -lt 5 ]; then
  echo "my number is less than 5";
else
 echo "my number is greater than 5";
fi
```

## Using conditionals in a loop

Here's a conditional statement used inside of a loop (don't forget to keep an eye on the required spaced inside the `[]`!):
```bash
for i in {1..50}; do
  if [ $i -le 25 ]; then
    echo "$i is <= 25";
  else
    echo "$i > 25";
  fi
done
```

## Building a program from pieces (and the weird modulo operator)

What does the following do?  And, what is the `%` operator:
```bash
for i in {1..50}; do
  result=$(($i % 2));
  if [ $result -ne 0 ]; then
    echo $i "odd";
  else
    echo $i "even";
  fi
done
```

## While loops

It's also possible to write `while` loops in `bash`.  IMO, these are not quite as easy to control in `bash` because you need to reach a specific ending point for the while loop to stop running, and it's sometimes easy to forget the ending condition, which means the loop runs continously until you stop it (that said, somethimes this is what you WANT to do).  Here's an example of what these sorts of loops look like:
```bash
i=0
while [ $i -lt 50 ]; do
  echo $i
  (( i++ ))
done
```
This same thing can also be accomplished with:
```bash
i=0
while [ $i -lt 50 ]; do
  echo $i
  i=$(( $i+1 ))
done
```
And we can do our even/odd computation the same way
```bash
i=0
while [ $i -le 50 ]; do
  result=$(($i % 2));
  if [ $result -ne 0 ]; then
    echo $i "odd";
  else
    echo $i "even";
  fi
  i=$(( $i+1 ))
done
```
