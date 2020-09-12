#!/usr/bin/env python3


import argparse

# Leet Speak Letter Chart
# e = 3, a=4, o=0, l=1
def leetSpeak(wordlistRead, wordlistWrite):
    ''' Convert each word to leet speak, ie: leet to l33t '''
    try:
        leetWord = ''
        fd = open(wordlistWrite, 'w')
        with open(wordlistRead, 'r') as f:
            for eachWord in f:
                for eachLetter in eachWord:
                    if eachLetter == 'e' or eachLetter == 'E':
                        eachLetter = '3'
                        leetWord += eachLetter
                    elif eachLetter == 'l' or eachLetter == 'L':
                        eachLetter = '1'
                        leetWord += eachLetter
                    elif eachLetter == 'a' or eachLetter == 'A':
                        eachLetter = '4'
                        leetWord += eachLetter
                    elif eachLetter == 'b' or eachLetter == 'B':
                        eachLetter = '8'
                        leetWord += eachLetter
                    elif eachLetter == 'o' or eachLetter == 'O':
                        eachLetter = '0'
                        leetWord += eachLetter
                    elif eachLetter == 's' or eachLetter == 'S':
                        eachLetter = '5'
                        leetWord += eachLetter
                    else:
                        leetWord += eachLetter
            fd.write(leetWord)
            fd.close()
    except FileNotFoundError as e:
        print("Wordlist selected is not found.")
    except PermissionError as e:
        print("Reading/Writing Error: Permission Denied")
    except:
        print("Unknown Error Occurred.")




parser = argparse.ArgumentParser() 

parser.add_argument('-w', '--wordlist', help='Wordlist to manipulate')
parser.add_argument('-o', '--output', help='Output filename')
parser.add_argument('-l', '--leetspeak', action="store_true", help='Leet Speak')


argparser = parser.parse_args()


if argparser.leetspeak:
    leetSpeak(argparser.wordlist, argparser.output)
