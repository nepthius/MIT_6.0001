# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Anish Dhanasekaran
# Collaborators : 
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "wordgame.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()
    fsum = 0
    ssum = 0

    
    #calculates the first component
    for letter in word:
        if letter == 'd' or letter == 'g':
            fsum += 2
        elif letter == 'b' or letter == 'c' or letter == 'm' or letter == 'p':
            fsum += 3
        elif letter == 'f' or letter == 'h' or letter == 'v' or letter == 'w' or letter == 'y':
            fsum += 4
        elif letter == 'k':
            fsum += 5
        elif letter == 'x' or letter == 'j':
            fsum += 8
        elif letter == 'q' or letter == 'z':
            fsum += 10
        elif letter == '*':
            fsum += 0
        else:
            fsum += 1
    
    '''
    if '*' in word:
        if 1 > (7*(len(word)-1) - 3*(n-len(word))):
            ssum = 1
        else:
            ssum = (7*(len(word)-1) - 3*(n-len(word)))
    '''
    
    if 1 > (7*len(word) - 3*(n-len(word))):
        ssum = 1
    else:
        ssum = (7*len(word) - 3*(n-len(word)))
    
    return fsum * ssum
        
        

    
    #pass  # TO DO... Remove this line when you implement this function

#print(get_word_score("Anime", 3))


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line
    

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3))

    for i in range(num_vowels):
        #print(i)
        #print(range(num_vowels))
        if i +1 == num_vowels:
            hand['*'] = hand.get('*', 0) +1
            break
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1

    return hand

#print(deal_hand(0))

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    
    wdic = get_frequency_dict(word.lower())
    ret_hand = hand.copy()

    for letter in wdic.keys():
        if letter in hand.keys():
            for x in range(wdic[letter]):
                ret_hand[letter] -= 1
                if ret_hand[letter] <= 0:
                    del ret_hand[letter]
                    break
    
    return ret_hand


    #pass  # TO DO... Remove this line when you implement this function

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    #print(word_list)
    word = word.lower()
    #print("\n\n\nIN WORD_LIST CONDITIONAL\n\n\n\n")

    wdic = get_frequency_dict(word)
    vword = ""

    if word.find('*') >= 0:
        for x in VOWELS:
            vword = word.replace('*', x)
            if vword in word_list:
                break
        if not vword in word_list:
            #print("\n\nWORD IN FALSE LOOP: ", vword)
            return False


    else:
        if not word in word_list:
            return False
    
    
    temp_hand = hand.copy()

    for letter in wdic.keys():
        if not letter in temp_hand.keys():
            #print("\n\nIN THE HAND LOOP\n\n")
            return False
        for x in range(wdic[letter]):
            temp_hand[letter] -= 1
            if temp_hand[letter] < 0:
                return False
        

    return True

    #pass  # TO DO... Remove this line when you implement this function



#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    fsum = 0

    for x in hand.keys():
        fsum += hand[x]


    return fsum
    
    pass  # TO DO... Remove this line when you implement this function


#hand = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's':1, 'z':1, 'y': 2}
#print(calculate_handlen(hand))

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """

    fsum = 0
    temp = 0

    while not hand == {}:

        print("\nCurrent Hand: ", end="")
        display_hand(hand)

        word = input("Enter a word, or \"!!\" to indicate that you are finished: ")
        
        if is_valid_word(word, hand, word_list):
            #print("\n\nis a valid word!\n\n")
            temp = get_word_score(word, calculate_handlen(hand))
            fsum += temp
            hand = update_hand(hand, word)  
            print("\"%s\"" %word, "earned", temp, "points. Total:", fsum)
            
            #print(word)
        elif word == "!!":
            break

        else:
            hand = update_hand(hand, word)
            print("That is not a valid word. Please choose another word.")

    if hand == {}:
        print("Ran out of letters. Total Score: ", fsum)
        
    else:
        print("Total Score: ", fsum)

    return fsum 



'''
Test case for function play_hand

hand = {'a': 1, 'c': 1, 'f': 1, 'i':1, '*':1, 't':1, 'x': 1}
word_list = load_words()
print(play_hand(hand, word_list))
'''


#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    fhand = hand.copy()
    letter_bank = ""

    if not letter in hand.keys():
        return fhand
    
    if not letter in CONSONANTS and not letter in VOWELS:
        return fhand

    for x in VOWELS:
        if not x in hand.keys() and not x == letter:
            letter_bank += x
    
    for x in CONSONANTS:
        if not x in hand.keys() and not x == letter:
            letter_bank += x

    nletter = random.choice(letter_bank)

    fhand[nletter] = fhand.pop(letter)



    return fhand

    pass  # TO DO... Remove this line when you implement this function

'''
TEST FOR SUBSTITUTE_HAND FUNCTION

letter = 'l'
hand = {'d':2, '*':1, 'l':1, 'o':1, 'u':1, 't':1}
print(substitute_hand(hand,letter))
'''

    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    hand = deal_hand(HAND_SIZE)
    total_hands = int(input("\nEnter total number of hands: "))
    counter = 0
    replay_counter = 0
    fsum = 0
    hsum = 0

    while counter < total_hands:
        hsum = 0
        print("Current hand: ", end="")
        display_hand(hand)
        sub = input("Would you like to substitue a letter? ")
        if sub[0] == 'y' or sub[0]=='Y':
            letter = input("Which letter would you like to replace: ")
            nhand = substitute_hand(hand, letter)
            hsum += play_hand(nhand, word_list)
        else:
            hsum += play_hand(hand, word_list)

        print("----------")

        if replay_counter == 0:
            replay = input("Would you like to replay the hand? ")

        if replay[0] == 'y' or replay[0] == 'Y':
            replay_counter += 1

        else:
            hand = deal_hand(HAND_SIZE)
            replay_counter = 0
            counter += 1
            fsum += hsum
        
        replay = "no"

    print("Total score over all hands: ", fsum)
    return fsum


        
   
    
   


   # print("play_game not implemented.") # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
