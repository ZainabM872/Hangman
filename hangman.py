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

    print("Welcome to the hangman game!")
    print("The game will run until you guess the word or run out of tries")
    print("Number of tries left ", displayHangman(tries))
    print(wordCompleted)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if(len(guess) == len(word) and guess.isalpha()):
            guessedWords.append(guess)
        elif (len(guess) == 1 and guess.isalpha()):
            for i in word:
                if i == guess and guess not in guessedLetters:
                    guessedLetters.append(guess)
                    wordCompleted = "_"
            if(guess in guessedLetters):
                print("You already guessed the letter ", guess)
                
            elif(guess not in word):
                print("Guess is not in the word ")
                tries -= 1
        else:
            print("Please enter a letter or word")

        print("Number of tries left ", displayHangman(tries))
        print(wordCompleted)


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
