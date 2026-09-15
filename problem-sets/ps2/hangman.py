# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import os
import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "words.txt")

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for char in secret_word:
      if char not in letters_guessed:
          return False
    return True    
    


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_progress = ""
    if len(letters_guessed)==0:
        for char in secret_word:
            word_progress += "*"
        return word_progress
    for char in secret_word:
        if char in letters_guessed:
            word_progress += char
        else:
            word_progress += "*"
    return word_progress


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = ""
    for l in string.ascii_lowercase:
        if l not in letters_guessed:
            available_letters += l
    return available_letters


def reveal_letter(secret_word, letters_available):
    """
    secret_word: string, the secret word to guess.
    letters_available: string of available lowercase letters
    Returns a letter that was not guessed by the user and is part of the secret word.
    """
    choose_from = ''
    for e in letters_available:
        if e in secret_word:
            choose_from += e

    new = random.randint(0, len(choose_from)-1)
    revealed_letter = choose_from[new]
    return revealed_letter


def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    in_play = True
    guesses_remaining = 10
    letters_guessed = []

    # Print out start message
    print("Welcome to hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    # Game mechanics
    while in_play:
        if guesses_remaining == 0:
            print(f"Sorry, you ran out of guesses. The word was {secret_word}")
            in_play = False
        else:
            # Print out current status of game to user
            print("--------------")
            # Check winning condition
            if has_player_won(secret_word, letters_guessed):
                print("Congratulations, you won!")
                print(f"Your total score for this game is: {(guesses_remaining + 4*len(set(secret_word))) + (3*len(secret_word))}")
                in_play = False
            else: 
                if guesses_remaining > 1:
                    print(f"You have {guesses_remaining} guesses remaining.")
                else:
                    print(f"You have {guesses_remaining} guess remaining.")

                print(f"Available letters: {get_available_letters(letters_guessed)}")

                # Get user input and check for validity
                new_letter = input("Please guess a letter: ").lower()
                if len(new_letter) == 1 and new_letter in string.ascii_lowercase:
                    # If letter is valid, check whether it was already guessed
                    if new_letter in letters_guessed:
                        print(f"Oops! You've already guessed the letter: {get_word_progress(secret_word, letters_guessed)}")
                    # If letter is new, check whether it is part of the secret word or not to give feedback to user
                    else: 
                        letters_guessed.append(new_letter)
                        if new_letter in secret_word:
                            # Letter is new and contained in secret word 
                            print(f"Good guess: {get_word_progress(secret_word,letters_guessed)}")
                        else: 
                            guesses_remaining -= 1
                            print(f"Oops! That letter is not in my word: {get_word_progress(secret_word,letters_guessed)}")
                elif new_letter == '!' and with_help:
                    # Implement help functionality in here
                    if guesses_remaining < 4:
                        print(f"Oops! Not enough guesses left: {get_word_progress(secret_word,letters_guessed)}")
                    else:
                        revealed_letter = reveal_letter(secret_word, get_available_letters(letters_guessed))
                        letters_guessed.append(revealed_letter)
                        guesses_remaining -= 3
                        print(f"Letter revealed: {revealed_letter}")
                        print(get_word_progress(secret_word, letters_guessed))
                else:
                    print(f"Oops! That is not a valid letter. Please input a letter from the alphabet: {get_word_progress(secret_word,letters_guessed)}")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

