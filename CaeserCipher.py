#!/usr/bin/env python
# Author: Rebecca Li
# Date: September 13,2014
#This program Caeser Cipher is written to encode and decode Text using R0T-13 method

import time   # Import the package time


# Create a dictionary for decoding
key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 
 'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}  

#Give the original code
sentence = 'Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!'

words = sentence.split()  #split the sentence into words
NewSentence = ''          #Create a new empty sentence

for word in words:
    for letter in word:
        if (letter =='?' or letter == "!"):   # When it comes to ! and ?, skip the decoding process
            NewSentence += letter
            break
        NewSentence += key[letter]            #Decoding process
    NewSentence += ' '                 # Create a space between each word
    
print 'The Top Confidential is loading...'
time.sleep(1)                    # Create 1 sesond delay
print 'The secret code means \"%s\"' %NewSentence 
