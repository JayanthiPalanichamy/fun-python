from WordGame import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#
def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    # TO DO...
    
    score=0
    for j in range(2,HAND_SIZE+1):
       permu=get_perms(hand, j)
       for i in permu:
         if i in word_list:
           a=get_word_score(i,HAND_SIZE)
           if a>score:
               score=a
               word=i  
    if score >0:
      return word
    else:
      return ''
 
        

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    # TO DO ...
    score=0
    hand1=hand.copy()
    while True:
     print "Current Hand:"
     display_hand(hand1)
     word=comp_choose_word(hand1, word_list)
     s=get_word_score(word, HAND_SIZE)
     score +=s
     print "Score of the word ",word," is ",s," Total: ",score
     hand1=update_hand(hand1,word)
     if len(hand)==0 or s==0:
         break
    
    
#
# Problem #6C: Playing a game
#
#
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    # TO DO...
    
    x=' '
    y=''
    while y !='x':
      print "\'u\': user play the game \n\'c\': computer play the game\n\'x\': to exit the game"
      y=raw_input("Enter your input: ")
      if(y=='u'):
        while x !='e':
         print" n:user play a new (random) hand \n r:the user play the last hand again \n e:exit the game"   
         x=raw_input( "Enter your input :")
         if x=='e':
           print "Game is exited"
           break
         elif x=='n':
           hand=deal_hand(HAND_SIZE)
           play_hand(hand,word_list)
         elif x=='r':
           play_hand(hand,word_list)
      elif y=='c':
        comp_play_hand(hand, word_list)
    
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    
