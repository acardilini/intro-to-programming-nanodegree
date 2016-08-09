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
medium_answer = ["panic", "inputs", "outputs", "optimize"]

parts_of_hard = ["__1__", "__2__", "__3__", "__4__"]
hard_answer = ["panic", "inputs", "outputs", "optimize"]

# The following are some test strings to pass in to the play_game function.
warm_up = """
An good guide for approaching problems is: 0. Don't __1__!!, 1. What are the __2__?, 2. What are the __3__?, 3. Work through some examples by hand., 4. Simple mechanical solutions, 5. Don't __4__ prematurely! Simple and correct is best, only do it when you need to.

"""

make_me_thinking = """"""

brain_sweats = """"""

# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.
def play_game(ml_string, parts_of_speech, answer, preamble):
    print preamble
    print ml_string
    replaced = []
    ml_string = ml_string.split()
    answer_no = 0
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            attempt = 3
            while attempt > 1:
                user_input = raw_input("What should " + replacement + " be replaced with? ")
                if user_input == answer[answer_no]:
                    word = word.replace(replacement, user_input)
                    replaced.append(word)
                    answer_no = answer_no + 1
                    print """Congratulations, you got it right!!"""
                    break
                else:
                    print "Ooops"
                    attempt = attempt - 1
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    print replaced
    return replaced

# MY CODE
# Choosing a game level.
def game_choice():
    user_input = raw_input("""Please choose how easy you want to take it:
     Warming Up, Now I'm Thinking or Brain Sweats

     """)
    if user_input == "Warm up":
        play_game(warm_up, parts_of_easy, easy_answer, easy_preamble)
    if user_input == "Make me think":
        play_game(make_me_think, parts_of_speech1, medium_answer, meadium_preamble)
    if user_input == "Brain Sweats":
        play_game(brain_sweats, parts_of_speech1, hard_answer, hard_preamble)

print game_choice()
