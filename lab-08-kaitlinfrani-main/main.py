# -*- coding: utf-8 -*-
"""
Kaitlin Frani
CPSC 223P-01
Wed Apr 7, 2021
kaitlinfrani@fullerton.edu
"""

import random

alphabet = "abcdefghijklmnopqrstuvwxyz"

# Hangman class
class Hangman:
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self, word, triesAllowed):
        self.word = word
        self.triesAllowed = triesAllowed
        
        #for get letters used, string
        self.letters_used = ""
        #to show word, need to list for index letters
        self.show_word = []
        for index in range(len(self.word)):
            self.show_word += "-"

    def Guess(self, letter):
        """Pass in a letter (length = 1) and check to see if it is in the word.
            If it is, replace blanks in display word with letter and return True
            If not, decrement the number of tries left and return False
        """
        replace_letter = False

        #1 letter
        if len(letter) != 1:
            return False
        #need to be a letter
        if letter not in alphabet:
        #if letter not in "abcdefghijklmnopqrstuvwxyz":
            return False
        else:
            for index in range(len(self.word)):
                if letter in self.word[index]:
                    self.show_word[index] = letter
                    #print("Good guess!")
                    replace_letter = True
        self.letters_used += letter
        
        if not replace_letter:
            print("Too bad!")
            self.triesAllowed -= 1
            return False
        else:
            print("Good guess!")
            return False

    def GetNumTriesLeft(self):
        """Return the number of tries left"""
        return self.triesAllowed
    
    def GetDisplayWord(self):
        """Return the display word (with dashes where letters have not been guessed)
        i.e. the word happy with only the letter 'p' guessed so far would be '--pp-'"""
        
        #need to use .join to convert list to string
        return ''.join(self.show_word)
    
    def GetLettersUsed(self):
        """Return a string with the list of letters that have been used"""
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
    wordFileList = wordFileText.split()
    randomIndex = random.randint(1, 222773)
    
    # Instantiate a game using the Hangman class
    game = Hangman(wordFileList[randomIndex], 8)
    
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Use a while loop to play the game
    while game.GetGameResult() is False:
        print("Here's your word so far: ", game.GetDisplayWord())
        print("You have", game.GetNumTriesLeft(), "guesses left.")
        print("Letters used: ", game.GetLettersUsed())
        #make sure input is lower
        letter = input("Guess a letter: ").lower()
        game.Guess(letter)
        alphabet = alphabet.replace(letter, "")
        print("")
        
    print("The word was " + game.word)
