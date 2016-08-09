# A list of replacement words to be passed in to the play game function.
parts_of_speech1  = ["PLACE", "PERSON"]#, "PLURALNOUN", "NOUN", "NAME", "VERB", "OCCUPATION", "ADJECTIVE"]
answer = ["Melbourne", "Person"]

# The following are some test strings to pass in to the play_game function.
test_string1 = "Hi, my name is PERSON and I really like to VERB PLURALNOUN. I'm also a OCCUPATION at PLACE."
test_string2 = """PERSON! What is PERSON going to do with all these ADJECTIVE PLURALNOUN? Only a registered
OCCUPATION could VERB them."""
test_string3 = "What a ADJECTIVE day! I can VERB the day off from being a OCCUPATION and go VERB at PLACE."

# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.
def play_game(ml_string, parts_of_speech, answer):
    print ml_string
    replaced = []
    ml_string = ml_string.split()
    answer_no = 0
    for word in ml_string:
        replacement = word_in_pos(word, parts_of_speech)
        if replacement != None:
            attempt = 3 # TEST LINE - REMOVE IF BREAKS
            while attempt > 1: # TEST LINE - REMOVE IF BREAKS
                user_input = raw_input("Type in a: " + replacement + " ")
                if user_input == answer[answer_no]: # TEST LINE - REMOVE IF BREAKS
                    word = word.replace(replacement, user_input) # TEST LINE - REMOVE IF BREAKS
                    replaced.append(word) # TEST LINE - REMOVE IF BREAKS
                    answer_no = answer_no + 1
                    print """Congratulations!! That's right."""
                    break
                else: # TEST LINE - REMOVE IF BREAKS
                    print "Try again"
                    attempt = attempt - 1
            #word = word.replace(replacement, user_input)
            #replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

print play_game(test_string1, parts_of_speech1, answer)
