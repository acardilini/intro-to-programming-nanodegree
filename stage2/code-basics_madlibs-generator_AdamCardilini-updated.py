# Need to add "os" and "sys" libraries in order to exit the game when it ends
import os
import sys

# Text asking for difficulty level
what_difficulty = """
Please choose how easy you want to take it - enter the corresponding number 1, 2 or 3:

1. Warm Up, 2. Make Me Thinking or 3. Brain Sweats

"""
# Incorrect difficulty level
difficulty_again = """
Oops, thats not an option. Please try again :D

"""


# Text asking for number of wrong guesses.
wrong_guesses_preamble = """
It's up to you to decide if you want to make it even harder or easier. Type in the number of wrong guesses you allow yourself before you fail the game.

"""

# A list of replacement words to be passed in to the play game function.
easy_preamble = """
You've chosen to take it easy this time and give your brain a chance to warm up. Good for you.

Fill in the blanks below:"""
parts_of_easy = ["__1__", "__2__", "__3__", "__4__"]
easy_answer = ["panic", "inputs", "outputs", "optimize"]

meadium_preamble = """
Good choice! This will definitely test you, but if you know your stuff you'll get there.

Fill in the blanks below:"""
parts_of_medium = ["__1__", "__2__", "__3__", "__4__"]
medium_answer = ["boxes", "CSS", "selector", "attribute"]


hard_preamble = """
I like your style - Go Hard or Go Home!

Fill in the blanks below:"""
parts_of_hard = ["__1__", "__2__", "__3__", "__4__"]
hard_answer = ["dynamic", "flexible", "validate", "refine"]

# The following are some test strings to pass in to the play_game function.
warm_up = """
A good guide for approaching coding problems is:
    0. Don't __1__!!,
    1. What are the __2__?,
    2. What are the __3__?,
    3. Work through some examples by hand,
    4. Simple mechanical solutions,
    5. Don't __4__ prematurely! Simple and correct is best, only do it when you need to.

"""

make_me_think = """
The internet is made up of a whole lot of __1__. The style of a HTML page is defined by the __2__ language. In order to 'speak' with the HTML page and style the elements you need to identify each element using a __3__. The style of the element is then controlled by providing a value for each __4__ of the element you want to change.

"""

brain_sweats = """
With the range of web browsing divices available, from desktops to smart phones, webpages must be __1__. A webpage should be built in a way that allows for the __2__ positioning of its elements. Before celebrating a coding job well done it's important that you __3__ your code to check that everything works in different environments. Remembering the process of 'code, test & __4__' will help you build a functional webpage.

"""

# Congatulations message
congrats = """
Congratulations, you got it right.

"""

# Try again message
try_again = """
Ooops, try again.

"""

# Game over message
game_over = """
Sorry, that's not correct and you've run out of attempts!

Have a think and try again later.

"""

# Game complete message
game_complete = """
Well done you've finish the game by filling in all of the words correctly!!!

"""

# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# Runs the guts of the game by looping though replacement strings and attempts.
def run_game(ml_split, parts_of_speech, ml_string, attempt, answer, answer_no):
    for word in ml_split:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            print ml_string
            while attempt >= 1:
                user_input = raw_input("What should " + replacement + " be replaced with? ")
                if user_input == answer[answer_no]:
                    ml_string = ml_string.replace(replacement, user_input)
                    answer_no = answer_no + 1
                    print congrats
                    break
                elif attempt == 1:
                    print game_over
                    sys.exit()
                print try_again
                attempt = attempt - 1
    print ml_string


# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.
def play_game(ml_string, parts_of_speech, answer, preamble):
    attempt = int(raw_input(wrong_guesses_preamble))
    print preamble
    ml_split = ml_string.split()
    answer_no = 0
    run_game(ml_split, parts_of_speech, ml_string, attempt, answer, answer_no)
    print game_complete
    sys.exit()

# MY CODE
# Choosing a game level.
def game_choice():
    difficulty = raw_input(what_difficulty)

    if difficulty == "1":
        play_game(warm_up, parts_of_easy, easy_answer, easy_preamble)
    elif difficulty == "2":
        play_game(make_me_think, parts_of_medium, medium_answer, meadium_preamble)
    elif difficulty == "3":
        play_game(brain_sweats, parts_of_hard, hard_answer, hard_preamble)
    else:
        os.system('cls')
        print difficulty_again
        game_choice()

print game_choice()
