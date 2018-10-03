# Problem Set 5: Ghost
# Name: 
# Collaborators: 
# Time: 
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
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

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()
wordlist.append('')

# TO DO: your code begins here!

def playerinfo():
    '''asks for the playernumber and returns a list from 1 to the playernumber'''
    print 'enter the amounts of players'
    while True:
        try:
            players = range(1,input()+1)
            break
        except:
            print 'try again'
    
    return players

def is_valid_word(fragment):
    """
    Returns True if fragment is in the word_list Otherwise, returns False.
    Does not mutate fragment
    
    fragment: string
    word_list: list of lowercase strings
    """
    #checks if the word is a real word in list
    if fragment in wordlist:
       return True
    else:
        return False

def fragment_still_valid(fragment):
    for word in wordlist:
        if fragment == word[:len(fragment)] or fragment == '':
            return True
    return False

def hasNumber(inputString):
    if any(char.isdigit() for char in inputString):
           return True
    else:
           return False

def letterinput(player):
    '''asks a player (number) a letter, checks if it is a single letter and makes it lowercase and returns it'''
    print 'player', player, 'type a letter'
    while True:
        letter = str(raw_input())
        
        if hasNumber(letter):
            print 'no numbers! try again'
        elif len(letter) == 1:
            break
        else:
            print 'try again'
    return letter

def Is_valid(string):
    '''checks a string to see if valid word and returns True if is or False if not'''
    for i in wordlist:
        if i == string:
            return True
    return False

#The Game

players = playerinfo()
string = ''
points = {}
gameON = True

for i in players:
    points['player ' + str(i)] = 0
while gameON == True:
    while fragment_still_valid(string):
        for number in players:
            print string
            player = number
            letter = letterinput(number)
            string += letter
            if Is_valid(string) and len(string) > 3:
                string = ''
                break
    print 'ade it'
    points['player ' + str(number)] = 1
    print points
    if 4 in points.values():
        print 'game over'
        gameON = False



    
    
    

        
