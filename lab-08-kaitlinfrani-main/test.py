# -*- coding: utf-8 -*-
"""
Kaitlin Frani
CPSC 223P-01
Wed Apr 7, 2021
kaitlinfrani@fullerton.edu
"""

import random

lowercase = "abcdefghijklmnopqrstuvwxyz"

# Hangman class
class Hangman:

    def __init__(self, word, triesAllowed):
        self.word = word
        self.triesAllowed = triesAllowed
        self.show_word = []
        self.letters_used = ""
        for index in range(len(self.word)):
            self.show_word += "-"

    def Guess(self, letter):
        """Pass in a letter (length = 1) and check to see if it is in the word.
            If it is, replace blanks in display word with letter and return True
            If not, decrement the number of tries left and return False
        """
        letterFound = False
        if len(letter) != 1:
            print("Please enter one leter")
            return False
        if letter not in lowercase:
            print("Enter a letter you havent used")
            return False
        
        else:
            for index in range(len(self.word)):
                if letter in self.word[index]:
                    self.show_word[index] = letter
                    letterFound = True
        self.letters_used += letter
        
        if not letterFound:
            self.triesAllowed -= 1
            return False
        else:
            return True

    def GetNumTriesLeft(self):
        """Return the number of tries left"""
        return self.triesAllowed
    
    def GetDisplayWord(self):
        """Return the display word (with dashes where letters have not been guessed)
        i.e. the word happy with only the letter 'p' guessed so far would be '--pp-'"""
        string_word = ''.join(self.show_word)
        return string_word
    
    def GetLettersUsed(self):
        """Return a string with the list of letters that have been used"""
        #self.letters_used += letter
        return self.letters_used

    def GetGameResult(self):
        """Return True if all letters have been guessed. False otherwise"""
        if self.GetNumTriesLeft() == 0:
            print("You lost.")
            return True
        
        if self.word == self.GetDisplayWord():
            print("You won.")
            return True
        
        else:
            return False
        
    def DrawGallows(self):
        """Optional: Return string representing state of gallows"""
        pass

# implement the logic of your game below
if __name__=="__main__":
    # Read all the words from the hangman_words.txt file
    wordFile = open("hangman_words.txt", "r")
    wordFileText = wordFile.read()
    wordFile.close()
    
    # Seed the random number generator with current system time
    random.seed()
    
    # Convert the string of words in wordFile to a list,
    # then get a random word using
    # randomIndex = random.randint(min, max)
    wordList = wordFileText.split()
    randomIndex = random.randint(0, 1)
    
    # Instantiate a game using the Hangman class
    game = Hangman(wordList[randomIndex], 9)
    
    # Use a while loop to play the game
    while game.GetGameResult() is False:
        print(game.GetNumTriesLeft())
        print("Please guess a letter.")
        print(game.GetDisplayWord())
        letter = input()
        game.Guess(letter)
        lowercase = lowercase.replace(letter,"")
        print("")
        
    print("The word was " + game.word)