# -*- coding: utf-8 -*-
"""
Kaitlin Frani
CPSC 223P-01
Wed March 3, 2021
kaitlinfrani@csu.fullerton.edu
"""

# Maybe you can use some functions from the string module
import string

# This is the function that you must write the code for
def numWordsSpoken(candidate, word):
    """"This is a doc string that describes the function. Change it to your liking.
    Something like: This function returns the number of times a given word was 
    spoken by a given speaker"""
    
    if candidate == 'Obama':
        return obamaSpeech[word]
    if candidate == 'Romney':
        return romneySpeech[word]


# This code will extract the data from the debate file and read it into one big
# string named debateString
debateFile = open("debate.txt", "r")
debateString = debateFile.read() 
debateFile.close()

# This code will extract the data from the stop words file and read it into one big
# string named stopWordsString
stopWordsFile = open("stopWords.txt", "r")
stopWordsString = stopWordsFile.read()
stopWordsFile.close()

# Start your code here
obamaSpeech = {}
romneySpeech = {}

removePunctuation = string.punctuation
lowerCase = debateString.lower()

#setting which words will go into which speaker
speaker = 0
#want to split string into a list
for word in lowerCase.split():
    #checking for the stopwords
    if word not in stopWordsString:
        if word == "obama:":
            speaker = 1
        elif word == "romney:":
            speaker = 2
        
        #want to return string from the dictionaries we created use translate
        #use maketrans due to the punctuations and the ''
        if speaker == 1:
            if word not in obamaSpeech.keys() and (word != "obama:"):
                separated = word.translate(str.maketrans('', '', removePunctuation))
                obamaSpeech[separated] = 1
            elif word in obamaSpeech.keys():
                separated = word.translate(str.maketrans('', '', removePunctuation))
                obamaSpeech[separated] = obamaSpeech[word] + 1
        elif speaker == 2:
            if word not in romneySpeech.keys() and (word != "romney:"):
                separated = word.translate(str.maketrans('', '', removePunctuation))
                romneySpeech[separated] = 1
            elif word in romneySpeech.keys():
                separated = word.translate(str.maketrans('', '', removePunctuation))
                romneySpeech[separated] = romneySpeech[word] + 1

#looping through dictionaries and sorting them
sortedObama = {key: obamaSpeech[key] for key in sorted(obamaSpeech, key=obamaSpeech.get, reverse=True)}
sortedRomney = {key: romneySpeech[key] for key in sorted(romneySpeech, key=romneySpeech.get, reverse=True)}

#sorting the list, counting in the tuple then append to add the words
obamaList = []
for key, value in sortedObama.items():
	tupleSort = value, key
	obamaList.append(tupleSort)

romneyList = []
for key, value in sortedRomney.items():
	tupleSort = value, key
	romneyList.append(tupleSort)

#format for the output
print("Obama")
counter1 = 0
#extracting 40 most used non-stopwords and their counts
for x in range(40):
	print(f"{obamaList[x][0]}:{obamaList[x][1]} ", end = "")
	counter1 = counter1 + 1
    #divide by 4 since we want four words per line
	if counter1 % 4 == 0:
		print()

print("\nRomney")
counter2 = 0
for x in range(40):
	print(f"{romneyList[x][0]}:{romneyList[x][1]} ", end = "")
	counter2 = counter2 + 1
	if counter2 % 4 == 0:
		print()