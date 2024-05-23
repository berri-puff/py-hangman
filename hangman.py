from words import words_list
import random

def get_word():
    word = random.choice(words_list)
    return word.lower()
