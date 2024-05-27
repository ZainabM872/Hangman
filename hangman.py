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