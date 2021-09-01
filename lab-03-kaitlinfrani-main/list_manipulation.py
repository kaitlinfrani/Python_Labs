# -*- coding: utf-8 -*-
"""

Kaitlin Frani
CPSC 223P-01
Wednesday Feb 10, 2021
kaitlinfrani@fullerton.edu

"""

fruits = ["grape", "mango", "nectarine", "pineapple", "banana", 
          "apple", "orange", "pear", "strawberry", "avocado"]

vegetables = ["zucchini", "asparagus", "kale", "spinach", "broccoli",
              "celery", "beets", "bok choy", "brussels sprouts", "arugula"]

#The program shall print the length of the combined list
combined_list = fruits + vegetables
length_list = len(combined_list)
print("There are " + format(length_list) + " elements in the combined list")

#The program shall sort the list alphabetically, then use a loop to print all 
#elements that start with a letter in the first half of the alphabet

#sorting the combined list alphabetically
sortedCombinedList = sorted(combined_list)

#make list of first half of alphabet
#loop to print all elements that start w/ letter in first half of alphabet
first_half = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
for letter in sortedCombinedList:
    if letter.startswith(tuple(first_half)):
        print (letter)

#The program shall reverse the order of the combined, sorted list and print
print(sortedCombinedList[::-1])