# Problem Set 2, hangman.py
# Name: Anish Dhanasekaran
# Collaborators: None

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import os

WORDLIST_FILENAME = "words.txt"
print(WORDLIST_FILENAME)


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    #print(os.getcwd())
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    if letters_guessed == []:
      return False

    for a in secret_word:
      for b in letters_guessed:
        if b == a:
          break
        if b == letters_guessed[-1]:
          return False
        
    
    return True

'''
Test case for is_word_guessed function 
#secret_word = 'apple'
#letters_guessed = ['a', 'p', 'p', 'l' , 'e']
#print(is_word_guessed(secret_word, letters_guessed))
'''

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    ret = ''
    for a in secret_word:
      for b in letters_guessed:
        if b == a:
          ret+=b
          break
        if b == letters_guessed[-1]:
          ret += '_ '
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    return ret

'''
Test case for get_guessed_word function
secret_word = 'apple'
letters_guessed = ['e', 'i', 'k', 'p' , 'r', 's']
print(get_guessed_word(secret_word, letters_guessed))
'''


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    ret = ''

    if letters_guessed == []:
      return string.ascii_lowercase
    for a in string.ascii_lowercase:
      for b in letters_guessed:
        if b == a:
          break
        if b == letters_guessed[-1]:
          ret += a
    return ret

    # FILL IN YOUR CODE HERE AND DELETE "pass"

'''
Test for get_available_letters fuction
letters_guessed = ['e', 'i', 'k', 'p' , 'r', 's']
print(get_available_letters(letters_guessed))
''' 

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    word = choose_word(wordlist)
    guesses_remaining = 6
    warnings_remaining = 3
 
    letters_guessed = []
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(word)} letters long.")
    print(f"You have {warnings_remaining} warnings left")
    #print(is_word_guessed(secret_word, letters_guessed))

    while not is_word_guessed(secret_word, letters_guessed) and guesses_remaining > 0:
      
      print("-------------")
      print(f"You have {guesses_remaining} guesses left.")
      print(f"Available letters: {get_available_letters(letters_guessed)}")
      user = input("Please guess a letter: ")

      if is_valid_input(user, letters_guessed):

        letters_guessed.append(user)
        
        if user in secret_word:
          print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
        
        else:
          print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
          guesses_remaining -= 1

        
        
      
      elif user in letters_guessed:
        warnings_remaining -= 1
        if warnings_remaining <= 0:
          print("Oops! You've already guessed that letter. You have 0 warnings left so you lose one guess: ", get_guessed_word(secret_word, letters_guessed))
          guesses_remaining -= 1
        else:
          print(f"Oops! You've already guessed that letter. You have {warnings_remaining} warnings left: ", get_guessed_word(secret_word, letters_guessed))

      else:
        warnings_remaining -= 1
        if warnings_remaining <= 0:
          print("Oops! That is not a valid letter. You have 0 warnings left so you lose one guess: ", get_guessed_word(secret_word, letters_guessed))
          guesses_remaining -= 1
        else:
          print(f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left: ", get_guessed_word(secret_word, letters_guessed))   
    
    if is_word_guessed(secret_word, letters_guessed):
      print("Congratulations, you won!")
      #print("Your total score for this game is: ", )
    
    else:
      print(f"Sorry, you ran out of guesses. The word was {secret_word}")
    pass

def is_valid_input(input, letters_guessed):
    '''
    This function makes sure that the input is acceptable and is not already guessed
    '''
    for a in string.ascii_lowercase:
      if input == a:
        break
      if a == string.ascii_lowercase[-1]:
        return False
    
    for b in letters_guessed:
      if input == b:
        return False
    
    return True

'''
Test case for is_valid_input

letters_guessed = ['e', 'i', 'k', 'p' , 'r', 's']
print("valid input: ", is_valid_input('e', letters_guessed))
'''

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)

