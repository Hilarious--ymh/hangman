def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True
    
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    # strings are immutable
    result=str()
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            result=result+' _'
        else:
            result=result+secretWord[i]
    return result
               
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    all_letters=string.ascii_lowercase
    copy_letters=all_letters[:]
    for i in range(len(copy_letters)):
        if copy_letters[i] in lettersGuessed:
            all_letters=all_letters.replace(copy_letters[i],'')
    print ('Available Letters:'+all_letters)       
    
    
    
    
    
def hangman(secretWord):
    global lettersGuessed
    lettersGuessed=list()
    counts=8
    while counts>=1 and getGuessedWord(selected_word,lettersGuessed)!=selected_word:
        print('You have %d guesses left.' % counts)
        getAvailableLetters(lettersGuessed)
        letter=raw_input('Please guess a letter: ')

        if letter in selected_word:
            if letter not in lettersGuessed:
                counts-=1
                global lettersGuessed
                lettersGuessed=lettertsGuessed+letter
                print 'Good guess:',getGuessedWord(selected_word,lettersGuessed)
            else:
                print "Oops! You've already guessed that letter:",getGuessedWord(selected_word,lettersGuessed)
        else:
            counts-=1
            print 'Oops! That letter is not in my word:',getGuessedWord(selected_word,lettersGuessed)
    if counts==0:
        print 'Sorry, you ran out of guesses. The word was else.'
        print selected_word
    else:
        print 'Congratulations, you won!'
            

import random
import string

WORDLIST_FILENAME = "words.txt"
selected_word=chooseWord(loadWords())
print 'Welcome to the game, Hangman!'
print ('I am thinking of a word that is %d letters long.' % len(selected_word))
hangman(selected_word)

    
    
    
    
    
    
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
