import random
import string
import re
from words import choose_word
from images import IMAGES

def print_image(wrong):
    if wrong != 0:
        print(IMAGES[wrong-1])


def is_word_guessed(secret_word, letters_guessed):
    return all(x in letters_guessed for x in secret_word)

def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    string = "".join(sorted(list(set(alphabets) - set(letters_guessed))))
    letters_left = string.lower()
    return letters_left


def isValid(given_input):
    pattern = re.compile("[a-z]")
    if len(given_input) == 1 and pattern.fullmatch(given_input) is not None:
        return True
    else:
        return False


def hangman(secret_word):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    letters_guessed = []
    wrong = 0
    chances = 1
    while True:
        print(f"Remaining Lives : {8 - wrong}")
        print_image(wrong)
        if wrong == 8:
            print("=========================[ GAME OVER ]=========================")
            print(f"Correct word was : {secret_word}")
            print("===============================================================")
            exit()
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {} ".format(available_letters))
        guess = input("Please guess a letter: ")
        letter = guess.lower()

        if guess == "hint":
            if chances > 0:
                chances = 0
                try:
                    pick = random.choice(letters_guessed)
                except IndexError:
                    pick = random.choice(secret_word)
                while pick in letters_guessed:
                    pick = random.choice(secret_word)
                print("HINT : ", pick)
                continue
            else:
                print("Hint Already Used!")
                continue

        if not isValid(guess):
            continue

        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                exit()
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            letters_guessed.append(letter)
            print("")
            wrong += 1


secret_word = choose_word()
hangman(secret_word)
