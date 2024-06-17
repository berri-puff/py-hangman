from words import words_list
import random

def get_word():
    word = random.choice(words_list)
    return word.lower()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_word = []
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
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == word]
                for index in indices:
                    word_as_list[index] == guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess == guessed_word:
                print("You already guessed the word")
                
            elif guess != word:
                print("That's not the word")
                tries -= 1
                guessed_word.append(guess)
            else:
                guessed = True 
                word_completion = word
        else: 
            print("Not a valid guess, try again!")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Yay! You guessed the word correctly")
    else:
        print("Sorry, you lose, the word was " + word )

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

def main():
    word = get_word
    play(word)
    while input("Play again? (Y/N)").upper()== "Y":
        word = get_word
        play(word)

if __name__ == "__main__":
    main()
