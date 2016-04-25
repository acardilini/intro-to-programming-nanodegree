# Udacity - Intro To Programming Nanodegree
## Stage 2 Notes
---
### 2.1 Introduction to Serious programming
The intention of this lesson is to learn about computer science and in particular,
how to solve problems by breaking them into smaller pieces and making them into
executable steps that can be solved by a computer.

#### What is Programming
Programming is the core of computer science, and allows us to tell a computer what to do.
Using programming we can tell a computer to do almost anything. To make a computer
do something useful we must tell it the computation steps it should take.

Python is a specific programming language that we can use to tell a computer what to do.
It is a high level language that is run in an interpreter, which converts the python code
to a language that the computer can interpret and passes this to the computer to run.

There are several ways to [think like a programmer](https://www.udacity.com/course/viewer#!/c-nd000/l-3521029360/m-3503049573) which helps with the process of writing
code. These include
1. Procedural thinking.
2. Abstract thinking.
3. Systems thinking.
4. Technological empathy.
5. Debugging.

#### Language Ambiguity
We invent new languages for writing programs because natural languages have inherent
ambiguity. Computers need to know exactly what we are telling them without ambiguity,
so programming languages have been developed in order to be exact when speaking to computers.

#### Grammar
Interpreters only know how to evaluate code that is part of the language being used. Each
program has grammar which defines the rules for communicating correctly in that
language.
---

### 2.2 Variables and Strings
This lesson focusses on a fundamental topic to programming, *the variable*, which is
often a very challenging concept to understanding for people learning programming.
During the lesson we will learn to answer the following questions about variables,
and hopefully help us understand this concept:
1. What is a variable?
2. What does it mean to assign a value to a variable?
3. What is the difference between what the equals = means in math versus in programming.
What's the difference between this: `2 + 3 = 5` and this: `my_variable = 5`?

#### Variables
Variables are created using assignment statements and allow you to assign a
value to a name.
> Name = Expression

After an assignment statement, the name on the left side refers to the value of
expression. This name can be used in the future in place of the assigned value.
The name can be any sequence of letters, numbers or underscores as long
as it starts with a letter or underscore.

#### Variables can Vary
It is possible to change the value of a variable by assigning a new
value to it. This can be very useful because it means we can iteratively change
the value of a variable. For example,
```python
hours = 9
hours = hours + 1
hours = hours * 2
```
In this code, after each line has been run the value of hours has changed
and the next line will be using the new value of hours to make the calculation. For each line hours is equal to, `9`, `10`, `20`.

When Python evaluate a line of code like the ones presented above, with `hour` on
each side of the `=`, it first evaluates the right hand side of the statement.
We know that this is the case because we must know what the right hand side of
the statement equals before we can assign it to the left hand side of
the statement.

#### Strings
A string is a sequence of characters surrounded by either single or double
qoutes, it doesn't matter which type but the starting and ending quote must
be the same type. It is also possible to create a multi-line string
by using TRIPLE quotes:
```Python
"""I am a string
and I span
multiple lines!
"""
```
Again the quotes can be either single (') or double ("). Assigning a string
to a variable is the same as
assigning a number to a variable. It is also possible to do string arithmatic
which results in the concatenation of strings. Both `+` and `*` can be used on
strings. Where `+` concatenates strings together, while `*` multiplies a string
at the same time as concatenating it.
```Python
day = "Friday"
print day + "is the last day working day of the week."
print friday * 3
```

#### Indexing Strings
It is possible to extract subsequences from a string by selecting parts of the string. This is because each part of a string is indexed, with the first character of a string being `0`. We specify the index we are after using `[NUMBER]`.
```Python
day = "Friday"
print day[0]
print day[1+1]
> F
> i
```
We can also select subsequences of continuous characters within a string
using `[START:STOP]`, where start and stop refer to the index values
for the first and last-1 characters you would like to extract. If either
side of the `:` is left blank it will default to the first or last index value.
```Python
day = "Friday"

> day
```
Understanding string indexing is important because it means that we can
begin to manipulate strings in useful ways.
```Python
day = "Friday"
print "Mon" + day[3:6]
```
If you use negative values when specifying an index it simply counts
in reverse from the end of the string.
```Python
day = "Friday"
print day[0:-1]
> Frida
```

#### Finding Strings in Strings
It is possible to find strings within larger sets of strings. This is
a standard Python method that is part of the base functions of Python. Find
is implemented using the following syntax `SEARCH.find(TARGET)`,
where SEARCH and TARGET specify the string we will be searching and
the target is what we are looking for. This will return the index position
of where the target string begins in the search string. If the string is
not found `-1` is output. It is important to remember that character case matters
when searching strings!
Within the method `.find(TARGET)` is a parameter, and there is a second
parameter that can be added to make this method even more powerful. The
second parameter tells `.find(TARGET, INDEX)` from which position to start
looking for the TARGET string.
```Python
woodchuck = "How much wood could a woodchuck chuck if a woodchuck could chuck wood"
print woodchuck.find("wood", 0)
> 9
print woodchuck.find("wood", 10)
> 22
```
#### Best Solutions
When writing code it is important to try to make the code work for
as many situations as possible. That is, where possible make your code
general so that it works in situations where your variables might change.

#### Replacing Strings
Another string method is `string.replace()` which does exactly what it
sounds like, it replaces strings. We parse two arguments to this method
and `old` string that we are wanting to replace and a `new` string that we
want to put in the `old` strings place, e.g. `SEARCH.replace('old', 'new')`.

### 2.3 Input -> Function -> output
This lesson focusses on an extremely important idea, *functions*. Functions
take input, run this through a set of procedures that is specified by
the function and then return output. The basic structure of a self defined
function in python looks like this:
```Python
def function_name(ARGUMENT):
  PROCEDURE
  return result_of_proceedure

print function_name()
```
`def` tells Python that we are about to define a function, and `return` actually
makes the result of the function accessible as output.

### 2.4 Control Flow & Loops: If and while
#### Equality Comparisons
There are several comparison operators that allow you to compare two values.
The output of a comparison is always a TRUE or FALSE value. Examples of comparison
operators include:
* '<' = Less Than
* '>' = Greater Than
* '!=' = not equal to
* '==' = equal to (we use '==' becuase '=' is used to assign values)

#### If Statements
In order to make our code do something depending on the result of a comparison
we need to use an `if` statement, which looks like:
```Python
if <TestExpression>:
  <Block>
```
Where <TestExpression> is our comparison statement and <Block> is that code
that runs depending on the result of the comparison. If the comparison result is
TRUE then the <Block> executes, if FALSE it doesn't execute. Code within
the <Block> is identified by it's indentation compared to the opening `if` line
of the statement. Here is an example of a function that uses an `if` statement:
```Python
def bigger(n1, n2):
    if n1 > n2:
        return n1
    return n2

print bigger(2,7)
print bigger(3,2)
print bigger(3,3)
```
An alternative method for executing this same function is to include an
`else` operator.
```Python
def bigger(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
print bigger(2,7)
print bigger(3,2)
print bigger(3,3)
```
Boolean comparison test also work on strings. For instance to test whether
a name starts with the letter 'D' we can use the following function.
```Python
def is_d(name):
    return name[0] == 'D'

print is_friend('Diane')
print is_friend('Fred')
```
Another important operator that allows us to build more complex functions is
`or`, which allows you to set multiple comparisons to test. It is important to
note that tests with an `or` operator will stop as soon as they find a
true statement. This is because, if the first value equates to 'True' there is
no need to evaluate the next value. Run the following code to see how `or`
this works:
```Python
def is_vowel(name):
  return name[0] == "A" or name[0] == 'E' or name[0] == 'I' or name[0] == 'O' or name[0] == 'U'
print is_vowel('Adam')
print is_vowel('Jess')
print is_vowel('Ulysses')
```
Telling a computer how to calculate something takes procedural thinking,
which means you need to break down the process into parts and tell
the computer to go through each part step-by-step. The following
function is a good example of doing this, as it gets the computer to
evaluate each input value in turn in order to determine the final result.
This function, takes in three values and returns the largest.
```Python
def biggest(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            return n1
    if n2 > n3:
        return n2
    else:
        return n3

print biggest(6,2,3)
print biggest(6,2,7)
print biggest(6,9,3)
print biggest(2,2,1)
```
This is quite a long function, and considering it is good good practice
to write short code we should attempt to do this. In a previous example
we created the function `bigger()` which determine the largest value
between two numbers. We can employ this function to make a much simpler
version of the `biggest()` function. The following image helps explain this
reasoning. ![bigger bigger biggest](http://lh4.ggpht.com/a8dcqarIbLzWtmXsdb4fUe5NjWatPlKWC8WHxowijH_LFw6cgzcbS-fCDfq8kUsLFVHOgxRBD2yR5BEGng)
The code looks like:
```Python
def biggest(n1, n2, n3):
  return bigger(bigger(n1, n2), n3)
```
What this function is saying is, determine which is the biggest out of
the first two values and then compare that with the third value and return
the biggest. And only in two lines.

Everything that can be computed mechanically by any machine can be described
by a program that only uses procedures, simple arithmetic, comparisons and `if` statements.
That's awesome!!!


#### While Loops
Loops allow you to do things over and over again, which can be very helpful
when you want to iterate something many times. A `while` procedure looks
very similar to the `if` procedure:
```Python
while <TestExpression>:
  <Block>
```
The difference is that if the <TestExpression> is True the <Block> will be
executed and start the `while` procedure again. An important idea
is introduced in by `while` loops, and that is having a changing <TestExpression>
which is done by initialising a value and changing it for each iteration of
the loop. For example:
```Python
def count():
  i = 0
  while i < 10:
    print 1
    i = i + 1
count()
```
In this example, `i` is changing with each iteration and the loop
continue until `i` = 10. It is very important to note that if the <TestExpression>
never equals False then the `while` loop will run forever. This is called
an infinite loop and can be really annoying.

This following example of a `while` loop removes all the spaces from a
string of text. Look at each section of this function and figure out how
it is doing this:
```Python
def remove_spaces(text):
    text_without_spaces = '' #empty string for now
    while text != '':
        next_character = text[0]
        if next_character != ' ':    #that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]
    return text_without_spaces
print remove_spaces("hello my name is andy how are you?")
```
To figure it out we need to break the function into parts, and see what
each part is doing. First we set up a variable called `text_without_spaces`
with the value of an empty string. We then start with `while text != ''` which is simply
saying, proceed with the while loop if the input is not an empty string. If we
have a string as input then we assign the first character of the string
to the variable `next_character`, and test whether this is a space or not.
If the first character of our string is not a space we concatenate it
to our `text_without_spaces` variable and reassign `text_without_spaces`
to this new variable. We then reassign out original `text` value to a string
without the first character and start the loop again. After there are
no characters left we return `text_without_spaces`.

#### Break statement
The break statement allows us to break out of the middle of a `while` loop even
if the `while` <TestExpression> is True. This looks like:
```Python
while <TestExpression>:
  <Code>
  if <BreakTest>:
    break
  <MoreCode>
<AfterWhile>
```

### 2.5 Debugging
No matter who you are, if you are writing code bugs happens! Because it
isn't possible to
avoid all possible errors the best way to deal with them is to have an
effective strategy for finding them.

#### Examine Error Messages
The most obvious type of bug is one that causes a funciton to crash and
produce an error message. These error messages will provide information
as to why the function crashed and can be helpful in finding bugs.
In python, error messages or 'Traceback' messages provide the line number at
which the function stopped running, and the name of the specific function
that was being run when it stopped working.

##### Work from a Working Example
It can be useful to base your code on working examples, though it's important to make sure the example works correctly.

#### Check Intermediate Results
It can be harder to fix code that is simply not working as expected compared
to code that throws an error. To figure the bug in the code in such cases
it can be useful to check how it is working throughout. Adding `print`
statements to intermediate steps within a function can be helpful for finding
tricky bugs.

#### Keep and Compare Old Versions
Using version control platforms like git can help you see changes in your
code that is causing bugs and also revert back to previous working versions.

#### Five Debugging Strategies
1. Examine error messages when programs crash
2. Work from example
3. Make sure examples work
4. Check (print) intermediate results
5. Keep and compare old versions

Debugging is an incredibly important part of software development, and
Udacity has another course that teaches the scientific approach to
[software debugging](https://www.udacity.com/course/software-debugging--cs259)

#### Writing Comments
It is important to write descriptive but unobtrusive comments in your
code to allow you to make notes to others and yourself about the code.
Some common guidelines for good commenting are:
1. Don't comment "obvious code."
2. Start functions with a comment.
  * Functions should start with a commnet describing input, output and what
  the function does. For example:
  ```python
  def bigger(n1, n2):
    # takes two numbers as input and outputs the biggest number.
    # identifies the biggest number.
  ```
3. Keep comments up-to-date
  * Code can become confusing if changes are made without updating comments.
4. Be concise


#### Random Noun
```python
from random import randint
def random_noun():
  random_num

```

<<<<<<< HEAD


### 2.6 Structured Data: Lists & For Loops
Lists are a sequence of any elements and can be created using square brackets:
e.g. `<LISTNAME> = ["<ELEMENT>", "<ELEMENT>"]`. This means that lists can
contain strings, numbers and other lists. List can be sliced and accessed in
the same way that strings can, by using index values.

#### Nested Lists
When a list is contained within a list it is still possible to access each
element. To do this you must use indexing to select the list your are
interested in and then use a second index to identify the element. For
instance the following code prints the name of the capital of India.
```python
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

print countries[1][1]
```

#### Mutation
It is possible to modify value of an element of a list after the list has
been created. This can be done by selecting an element of a list and
assigning a new value to this element.
```python
stooges = ['Moe','Larry','Curly']
stooges[2] = 'Shemp'
print(stooges)
```
When an element of a list is changed it will also effect the value
of the element in any other variable it is linked to.



The differences between a String and List include:
1. List elements can contain more than just characters.
2. Lists are mutable.

#### Aliasing
If two variable names refer to the same list object, any changes to one will
also occur in the other.

#### List Operations
There are several useful list operators that allow you to work more easily
with lists. Some of these include:
* `<LIST>.append(<ELEMENT>)` adds a new element onto the end of a list.
* `+` joins lists together, e.g. `[1,2] + [3,4]`
* `len(<LIST>)` determines the length of a list, i.e. how many elements a
list has.
There is an important different between `append` and `+` that it is worth
pointing out. Append adds a new element to the end of a list whereas `+` joins
two lists together. If you append a list to another list then you will end up
with a nested list.

#### For Loops
`for` statements allow you to iterate through a list of elements more
easily than using a while loop. These statements have the following expression:
```python
for <NAME> in <LIST>:
  <BLOCK>
```
Where `<NAME>` refers to each element within the list. The `for` loop starts
witht the first element, runs through the `<BLOCK>` and then goes onto
the next element, for all elements in the list. The following
function uses a `for` loop to calculate the sum of a list of values:
```python
def sum_list(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum

print sum_list([1,7,4])
```
The operation `<LIST>.index(<ELEMENT>)` returns the first place in
a list that an element in found. The problem with `.index` is that it returns
an error if the element you are trying to find is not in the list.
An alternative method is to use the `in` operator which tells you whether
an element is in a list by returning a boolean value. Another similar operator
is `not it`.

### How to Solve Problems
=======
## 2.5 How to Solve Problems
An important guide to approaching problems is:
0. Don't Panic!!
1. What are the inputs?
2. What are the outputs?
3. Work through some examples by hand.
4. Simple mechanical solutions.
5. Don't optimize prematurely! Simple and correct is best, only optimize
when you need to.

Assertions should be added to programs in order to maintain assumptions. These
can be included using `assert <expression>`. If the expression is incorrect
it will jump out of the program as if an error has occurred.
>>>>>>> 4a9315f8d889f8c0d605d02dad775e9bd89762e3

### Quizzes: Tips and hints
* `+=` adds the next number to an object.

#### Quiz: While Loop 2
```python
import random
random_list = []
list_length = 20

while len(random_list) < list_length:
  random_list.append(random.randint(0,10))    

# My code.
count = 0
i = 0
while i < 20:
    if random_list[i] == 9:
        count = count + 1
        i = i + 1 # DONT NEED THIS SECTION!
    i = i + 1
#

print random_list
print count
```

#### Quiz: While Loop 3
We now want to create a new list that contains the counts
of all occurrances of every number seen in the randomly generated
list. That means we want counts of all occurrences of all numbers
from 0 through 10 in our randomly generated list.
```python
import random
random_list = []
list_length = 20
while len(random_list) < list_length:
  random_list.append(random.randint(0,10))

# My code
count_list = [0] * 11
i = 0
while i < 20:
  # The answer inlcuded a variable 'number = random_list[i]' and put number in
  # the code.
  count_list[random_list[i]] = count_list[random_list[i]] + 1
  i = i + 1
#

print count_list
print sum(count_list)
```

#### Quiz: While Loop 4
We want to create a nicely formatted table that shows the number and its
corresponding count.
* This is a nice quiz because it makes you think about the spacing required
before the numbers are printed.
```python
import random

random_list = []
list_length = 20

while len(random_list) < list_length:
    random_list.append(random.randint(0,10))

count_list = [0] * 11
index = 0

while index < len(random_list):
    number = random_list[index]
    count_list[number] = count_list[number] + 1
    index = index + 1

print index

# My code
i = 0
print "number | occurences"
while i < len(count_list):
    spaces = len("number") - len(str(i))
    print " "*spaces + str(i) + " | " + str(count_list[i])
    i = i + 1

# My code
i = 0
print "number | occurences"
while i < len(count_list):
    spaces = len("number") - len(str(i))
    print " "*spaces + str(i) + " | " + "*"*count_list[i]
    i = i + 1

```
