# -*- coding: utf-8 -*-
"""
Kaitlin Frani
CPSC 223P-01
2/2/2021
kaitlinfrani@fullerton.edu
"""

import sys

# This is my second Python program. It inspects strings.

sentence = sys.argv[1]
word = sentence.split(" ")
largest = small = word[1]

for i in range(1,len(word)):
    if len(largest) < len(word[i]):
        largest = word[i]
    if len(small) > len(word[i]):
        small = word[i]

#printing out shortest word
print("Shortest word: " + small)
min = len(small)
if min > 1:
    print("It is " + format(min) + " characters")
    
else:
    print("It is " + format(min) + " character")
    
#printing out longest word
print("Longest word: " + largest)
max = len(largest)
if max > 1:
    print("It is " + format(max) + " characters")
    
else:
    print("It is " + format(max) + " character")