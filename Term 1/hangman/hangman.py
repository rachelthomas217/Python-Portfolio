#Rachel Thomas
#10/9/2019
#Hangman



#imports
import random

#constants
HANGMAN = ("""
------
 |    |
 |
 |
 |
 |
 |
 |
 |
_______
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
_______
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
_______
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
_______
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |   
 |   
 |   
 |   
 |   
_______
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |    |
 |   
 |   
 |   
 |   
_______
""",
"""
 ------
 |    |
 |    O
 |  /-+-\\
 |     |
 |     |
 |    | |
 |    | |
 |  
_______
""")

MAX_WRONG = len(HANGMAN) -1

WORDS = ("GUESS","BAND","PYTHON","PRACTICE","ZELDA")

#initialize variables
word = random.choice(WORDS) #the word to be guessed
so_far = "_" * len(word) #one dash for each letter
wrong = 0 # number of wrong guesses player has made
used = [ ]
#letters already guessed

print("Welcome to Hangman. Good luck!")

while wrong < MAX_WRONG and so_far != word:

    print(HANGMAN[wrong])
    print("\nYou've used the following letters: \n", used)
    print("\nSo far, the word is:\n", so_far)

    guess = input("\n\nEnter your guess; ")
    guess = guess.upper( )
    
    while guess in used:
        print("You've already guessed the letter", guess)
        guess = input("n\n\nEnter your guess: ")
        guess = guess.upper( )
        
    used.append(guess)
    if guess in word:
        print("\nYes!", guess, "is in the word!")

        new = " "
        for i in range(len(word)):
            if guess == word[i] :
                new+= guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nSorry,", guess, "isn't in the word. ")
        wrong += 1

            
    
