# Lesson 2.1: Introduction to Serious Programming

# Programming is grounded in arithmetic, so it's important
# to know how programming languages do simple math.
# Thankfully, Python follows the same math rules people do.
# See if you can predict the output of this code.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4180729266/m-48652460

print 3
print 1 + 1

# Add your own code and notes here.


# Lesson 2.2: Variables

# Programmers use variables to represent values in their code.
# This makes code easier to read by telling others what values
# mean. It also makes code easier to write by cutting down on
# potentially complicated numbers that repeat in our code.

# We sometimes call numbers without a variable "magic numbers"
# It's best to reduce the amount of "magic numbers" in our code

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48660987

speed_of_light = 299792458.0
billionth = 1.0 / 1000000000.0
nanostick = speed_of_light * billionth * 100
print nanostick

# Add your own code and notes here

# Lesson 2.2: Strings

# Strings are sequences of characters that are enclosed in quotes.
# We can enclose them with single or double quotes and assign them
# to variables. We can even combine strings by adding them (we call
# this concatenation).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48700403

print 'Hello'
print "Hello"

hello = "Howdy"
print hello * 3 - hello

# Add your own code and notes here

day = "Friday"
print day[3]
print day[1+1+1]
print (day+day)[0]

day = "Friday"
print day[0:-1]

day = "Friday"
print "Mon" + day[3:6]

dog = "dog1 dog2 dog3 dog4 dog5"
print dog.find("dog", 10)

woodchuck = "How much wood could a woodchuck chuck if a woodchuck could chuck wood"
print woodchuck.find("wood", 0)
print woodchuck.find("wood", 10)


# Lesson 2.3: Procedures

# Functions (also known as procedures or methods) take input and return an output.
# Programmers use functions all the time! They may seem confusing at first but
# the more you use and make them, the better you'll get!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4141089439/m-48667860

def rest_of_string(s):
    return s[1:]

print rest_of_string('audacity')

# Add your own code and notes here

a = 2
def sum(a, b):
    a = a + b
print sum(1,2)



def double1(x):
    return 2*x
print double1(3)

def double2(x):
    print 2*x
print double2(3)

def double3(x):
    return 2*x
    print 2*x
print double3(3)

def double4(x):
    print 2*x
    return 2*x
print double4(3)



# Lesson 2.4: Making Decisions - If Statements

# We'll often write programs that need to make comparisons between values.
# We can do comparisons just like we do in math with the < and > signs.
# We can also do equality comparisons with != (not equal) and ==.
# Comparisons always return a Boolean value (either True or False).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48727556/m-48724313

print 2 < 3
print 21 < 3
print 7 * 3 < 21
print 7 * 3 != 21
print 7 * 3 == 21

# Add your own code and notes here
print "Example 1: Greater-than and less-than comparisons"
print 2 > 1
print 1 > 2
print 5 < 20
print 100 < 19


print "Example 2: Equality and non-equality comparisons"
print 5 == 5
print "hello" == "hello"
print 5 == 10
print 5 == '5' # what do you think will happen here?
print 7 != 10
print 7 != 7


print "Example 3: A demo of what you are about to learn"
if 3 < 5:
    print "Three is definitely smaller than 5!"

if 10 > 20:
    print "Did you know that 10 is greater than 20!?"
else:
    print "20 is greater than 10"


def bigger(n1, n2):
    if n1 > n2:
        return n1
    return n2

print bigger(2,7)
print bigger(3,2)
print bigger(3,3)

def bigger(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
print bigger(2,7)
print bigger(3,2)
print bigger(3,3)

def is_friend(name):
    return name[0] == 'D'

print is_friend('Diane')
print is_friend('Fred')

name = 'Diane'
print name[0] == 'D'

def is_vowel(name):
  return name[0] == "A" or name[0] == 'E' or name[0] == 'I' or name[0] == 'O' or name[0] == 'U'
print is_vowel('Adam')
print is_vowel('Jess')
print is_vowel('Ulysses')

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


# Lesson 2.4: While Loops

# Loops are an important concept in computer programming.
# Loops let us run blocks of code many times which can be
# really useful when we have to repeat tasks.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48686708/m-48480488

def count():
    i = 0
    while i < 10:
        print i
        i = i + 1

count()

# Add your own code and notes here

i = 0
while i < 10:
  print 1
  i = i + 1


def remove_spaces(text):
    text_without_spaces = '' #empty string for now
    while text != '':
        next_character = text[0]
        if next_character != ' ':    #that's a single space
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]
    return text_without_spaces
print remove_spaces("hello my name is andy how are you?")

def print_numbers(x):
    i = 1
    while i <= x:
        print i
        i = i + 1

print_numbers(8)

def median(n1, n2, n3):
    # Takes three numbers as inputs and outputs the median value.
    if n1 < n2 < n3:
        return n2
    if n2 < n1 < n3:
        return n1
    else:
        return n3
print median(1, 2, 3)
print median(9, 3, 6)
print median(7, 8, 7)



# Let's put it all together. Write code for the function process_madlib, which takes in
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"

def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]

def process_madlib(mad_lib):
    processed = ""
    i = 0
    box_length = 4
    while i < len(mad_lib):
        frame = mad_lib[i:i+box_length]
        to_add = word_transformer(frame)
        processed = processed + to_add
        if len(to_add) == 1:
            i = i + 1
        else:
            i = i + 4
    return processed
    # your code here
    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len

test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)


# Lesson 2.6: Structured Data - Lists

# Similar to how strings are seuqences of characters, lists are
# sequences of anything! We can have lists of numbers, lists of
# characters, even lists of lists! And we can mix up the contents
# too so we can have lists containing many different things.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4180729266/m-48652460

p = ['y', 'a', 'b', 'b', 'a', '!']
print p
print p[0]
print p[2:4]

# Add your own code and notes here

stooges = ['Moe', 'Larry', 'Curly']

# Days in Month
# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(n):
    return days_in_month[n-1]


print how_many_days(1)
#>>> 31

print how_many_days(9)
#>>> 30


spy = [0,0,7]
def replace_spy(list):
    list[2] = list[2]+1
    return list
print spy
replace_spy(spy)
print spy


# Lesson 2.6: For Loops

# For loops, like while loops, are useful for running a block of code
# multiple times. For loops make iterating through elements in a list
# easier than using a while loop.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4152219158/m-48204891

def print_all_elements(p):
    for e in p:
        print e

myList = [1, 2, [3, 4]]
print_all_elements(myList)

# Add your own code and notes here

def sum_list(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum

print sum_list([1,7,4])

# Measure Udacity Quiz
def measure_udacity(list):
    sum = 0
    for i in list:
        if i[0] == 'U':
            sum = sum + 1
    return sum
print measure_udacity(["Dave", "Sebastian", "Katy"])
print measure_udacity(["Umika", "Umberto"])


# Find Element Quiz
def find_element(list, value):
    i = 0
    for e in list:
        if e == value:
            return index
        i = i + 1
    else:
        return -1

print find_element([1,2,3], 3)
print find_element(["alpha", "beta"], "gamma")

print [1,2,3].index(4)

def find_element(list, value):
    if value in list:
        return list.index(value)
    else:
        return -1
print find_element([1,2,3], 3)
print find_element(["alpha", "beta"], "gamma")

# Age in Days Problem
