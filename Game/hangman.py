# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

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
    for i in secret_word:
        if i not in letters_guessed:
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
    x=[]
    for i in secret_word:
        if i in letters_guessed:
            x.append(i)
        else:
            x.append('*')
    return ' '.join(x)
            


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    alphabet = list(string.ascii_lowercase) #in python strings are immutable (cannot be changed once created)
    for i in letters_guessed:
        alphabet.remove(i)       
    return ' '.join(alphabet)

def unique_letters(secret_word):
    """
    secret_word: str word to examine
    returns: int, number of unique letters in a word
    """
    u= set(secret_word) # set converts the string into a set of unique characters
    return len(u)

def helper(secret_word, letters_guessed):
    available = get_available_letters(letters_guessed).replace(" ", "")  # call the function, get available letters without spaces
    choose_from = ""
    for letter in secret_word:
        if letter in available and letter not in letters_guessed:
            if letter not in choose_from:
                choose_from += letter
    if choose_from == "":
        return None
    new = random.randint(0, len(choose_from) - 1)
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
    print ('Welcome to Hangman!')
    print (f'I am thinking of a word that is {str(len(secret_word))} letters long')
    print ('-----------')
    mistakesMade = 0
    letters_guessed =[]
    vowel = 'aeiou'
    while mistakesMade<10:
        if has_player_won(secret_word, letters_guessed) == False:
            print(f'you have {str(10-mistakesMade)} guesses left.')
            print(f'Available letters: {get_available_letters(letters_guessed)}')
            alphabet = list(string.ascii_lowercase)
            guess = input('Please guess a letter: ') # Remove the print inside input as it will return None
            x=guess.strip().lower() # Turn all input letters lowercase

            if x =='!': # Activate help
                if not with_help:
                    r= input ('Help is not enabled for this game. Do you wish to enable help?: ')
                    if r.strip().lower() == 'yes':
                        with_help = True
                    else:
                        print('Help remains disabled.')
                        print ('-----------')
                        continue
                if (10-mistakesMade)<3:
                    print(f'Oops! Not enough guesses left: {str(get_word_progress(secret_word, letters_guessed))}')
                    print('-----------')
                    continue
                revealed_letter = helper(secret_word, letters_guessed)
                letters_guessed.append(revealed_letter)
                print(f'Letter revealed: {revealed_letter}')
                print(get_word_progress(secret_word, letters_guessed))
                print('-----------')
                mistakesMade+=3
                continue # To skip further procerssing for the help input

            if len(x) !=1 or x not in alphabet:
                print(f'Oops! That is not a valid letter. Please input a letter from the alphabet: {str(get_word_progress(secret_word, letters_guessed))}')
                print ('-----------')
                continue

            if x in letters_guessed:
                print(f"Oops! You've already guessed that letter: {str(get_word_progress(secret_word, letters_guessed))}")
            else:
                letters_guessed.append(x)
                if x in secret_word:
                    print(f'Good guess: {str(get_word_progress(secret_word, letters_guessed))}')
                else:
                    print(f'Oops! That letter is not in my word: {str(get_word_progress(secret_word, letters_guessed))}')
                    if x in vowel:  # Check for strings and not int so use in vowel instead of == vowel
                        mistakesMade+=2
                    else:   
                        mistakesMade +=1
            print('-----------')
        else:
            score = (10-mistakesMade)+(4*int(unique_letters(secret_word)) + (3*len(secret_word)))
            print('Congratulations, you win!')
            print(f"Your total score for this game is {int(score)}")
            break

    if mistakesMade == 10:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')

    # FILL IN YOUR CODE HERE AND DELETE "pass"



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
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

