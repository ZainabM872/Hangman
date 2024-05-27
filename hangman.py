import random
from words import word_list #from words file

#getWord: returns a word to guess
def getWord():
    word = random.choice(word_list)
    return word.upper() #return the chosen work in uppercase to make comparison easier.

#
def play(word):
    wordCompleted = "_" * len(word) #initialize the word with _ for evry unguessed letter
    guessed = False
    guessedLetters = [] #holds the letters the user guesses
    guessedWords = [] #holds the words the user guessed to avoid repeats
    tries = 6 #number of body parts left to be drawn on hangman before user loses

#displays the hangman in different stages as the user guesses
#needed help from: https://github.com/kiteco/python-youtube-code/blob/master/build-hangman-in-python/hangman.py
def displayHangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries] #depending on how many tries are left, it returns an index in the list
