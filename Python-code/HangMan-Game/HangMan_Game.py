
# Hangman
"""Hangman is a paper and pencil guessing game for two or more players.
One player thinks of a word, phrase or sentence and the other tries to guess it by suggesting letters or numbers,
within a certain number of guesses.In this problem, the second
player will always be the computer, who will be picking a word at random.  """

import random
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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    
    wordlist = string.split(line)
    
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
def generate(a,b,c):
    index = 0
    ltuple1=()
    while index < len(a):
       index = a.find(c, index)
       if index == -1:
            break
       ltuple1 =ltuple1+(index,)
       index += 1
    for i in ltuple1:
        b[i]=c
    return b


wordlist = load_words()
a=choose_word(wordlist)
b=[]
for i in range(len(a)):
    b.append('_')


print "Welcome to the game, Hangman!"
print "I am thinking of a word that is ",len(a)," letters long"

chances=8
str='abcdefghijklmnopqrstuvwxyz'
str1=list(str)
while chances>0:
       newword=''.join(b)
       print  "-------------"
       print "You have ",chances," guesses left."
       print "Available letters: ",''.join(str1)
       guess=raw_input("Please guess a character: ")
       if guess in str1:
         if guess in a:
           newword1=generate(a,b,guess)
           newword=''.join(newword1)
           print "Good guess: ",newword
           str1.remove(guess)
           if '_' not in newword:
               print "------------"
               print "Congratulations, you won!"
               break
         else:
           chances -=1
           str1.remove(guess)
           print "Oops! That letter is not in my word: ",newword
if '_' in newword:
    print "Better luck next time ,The word is : ",a
           


    




