import random
from words import word_list #from words file

#getWord: returns a word to guess
def getWord():
    word = random.choice(word_list)
    return word.upper() #return the chosen work in uppercase to make comparison easier.