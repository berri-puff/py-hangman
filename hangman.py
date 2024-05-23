from words import words_list
import random

def get_word():
    word = random.choice(words_list)
    return word.lower()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_ word = []
    tries = 6
    print("Let's start a game of Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while guessed and tries > 0:
        guess = input('Please enter a letter or word: ').lower()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed this: ", guess)
            elif guess not in word:
                print("This word does not contain", guess)
                tries -= 1
                guessed_letters.append(guess)
            else: 
                print("Yay! ", guess, " is in the word!")
                guessed_letters.append(guess)
        elif len(guess) == len(word) and guess.isalpha():
        
        else: 
            print("Not a valid guess, try again!")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

def display_hangman(tries):
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
    return stages[tries]
