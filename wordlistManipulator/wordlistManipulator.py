#!/usr/bin/env python3

'''
Wordlist Manipulator 

Author: eof0100
Contact: eof0100@hackersareus.com


My first official python project. This script
will manipulate existing wordlists s9uch as making
words into uppercase, lowercase, capitalize the 
first letter, etc.


Notes to self
-----------------
prefix - group of letters (or an affix) that's added to beginning of a word
suffix - is an affix that's added to the end of a word
prefix - modifies the meaning of a word ie: make a word negative, show repition, or show opinion
         negate a word: word: kind adding prefix of 'un' negates a word to unkind, opposite of kind

Ideas to manipulate a word:
    prefix
    suffix
    combine two wordlists 


'''


import re
import argparse 



__version__ = 1.0



def CapFirstLetter(wordlistRead, wordlistWrite):
    '''Read existing wordlist, capitalize each word per line, write to new wordlist'''
    fd = open(wordlistWrite, 'w')
    with open(wordlistRead, 'r') as f:
        for eachWord in f:
            cap=eachWord.title()
            fd.write(cap)
        fd.close()
    

def CapAllLetters(wordlistRead, wordlistWrite):
    '''Read from an existing wordlist, capitalizing all letters, write to new wordlist'''
    fd = open(wordlistWrite, 'w') 
    with open(wordlistRead, 'r') as f:
        for eachWord in f:
            cap = eachWord.upper()
            fd.write(cap)
        fd.close()


def LowercaseAllLetters(wordlistRead, wordlistWrite):
    fd = open(wordlistWrite, 'w')
    with open(wordlistRead, 'r') as f:
        for eachWord in f:
            lowercase = eachWord.lower()
            fd.write(lowercase)
        fd.close() 


def WPA(wordlistRead, wordlistWrite):
    '''Make a WPA/WPA2 wordlist from an existing wordlist 8 <= x <= 64'''
    fd = open(wordlistWrite, 'w')
    with open(wordlistRead, 'r') as f:
        for eachLine in f:
            # only write words that are between 8 and 63 characters
            # note using 9 and 64 b/c \n is counted as a character
            if len(eachLine) >= 9 and len(eachLine) <= 64:
                fd.write(eachLine) 
            else:
                pass 
        fd.close()



def MixCaseUpperToLower(wordlistRead, wordlistWrite):
    '''From existing wordlist will convert each words case starting from Uppercase to lower and repeat'''
    fd = open(wordlistWrite, 'w')
    mix_case = ''
    with open(wordlistRead, 'r') as f:
        for word in f:
            i = True # capitalize
            for letter in word:
                if i:
                    mix_case += letter.upper()
                else:
                    mix_case += letter.lower()
                if letter != ' ':
                    # if not whitespace inverse bool value of i
                    i = not i
        fd.write(mix_case)
        fd.close() 
            


def MixCaseLowerToUpper(wordlistRead, wordlistWrite):
    '''From existing wordlist will convert each words case starting from Uppercase to lower and repeat'''
    fd = open(wordlistWrite, 'w')
    mix_case = ''
    with open(wordlistRead, 'r') as f:
        for word in f:
            i = False # begin with lowercase
            for letter in word:
                if i:
                    mix_case += letter.upper()
                else:
                    mix_case += letter.lower()
                if letter != ' ':
                    # if not whitespace inverse bool value of i
                    i = not i
        fd.write(mix_case)
        fd.close()


def Suffix(wordlistRead, wordlistWrite, suffix_word):
    '''Function will read an existing wordlist and suffix user specified text
       and then write the contents to a newly created wordlist with a name of users choice'''
    new_word = ''
    new_line = '\n'
    fd_write = open(wordlistWrite, 'w')
    with open(wordlistRead, 'r') as f:
        for word in f:
            # Remove \n from each word since we are adding a text after if I didn't
            # remove newline the newly added suffix  would be on the next line
            strip_word = word.strip() 
            new_word = new_word+strip_word+suffix_word+new_line
    fd_write.write(new_word)
    fd_write.close()



def Prefix(wordlistRead, wordlistWrite, prefix_word):
    '''Function will read an existing wordlist and prefix user specified text
       and then write the contents to a newly created wordlist with a name of users choice'''
    new_word = ''
    fd_write = open(wordlistWrite, 'w')
    with open(wordlistRead, 'r') as f:
        for word in f:
            new_word = new_word+prefix_word+word
    fd_write.write(new_word)
    fd_write.close()



def CombineTwoWordlists(




# ----- Testing out functions --------------
#user_input = str(input('Text to prefix:  '))
#Prefix('wordlist.txt', 'wordlist.prefix', user_input)

#user_input2 = str(input('Text to suffix:  '))
#Suffix('wordlist.txt', 'wordlist.suffix', user_input2)

#MixCaseUpperToLower('wordlist.txt', 'wordlist.upperTOlower')
#MixCaseLowerToUpper('wordlist.txt', 'wordlist.lowerTOupper')

