# Lab - 02 (Strings)

In this lab you will write another simple Python program; but this time it will do a little more than print "Hello, world!".  This exercise is intended to get you started using Python variables and working with strings.  In the process you will likely need to use some basic Python language constructs such as loops, module imports and built-in functions.

# Requirements

Your software will read a sentence from the command line, identify the longest and shortest word, and display those words along with their character count. Your output must match the expected output exactly to be given full credit. Specifically, here are the requirements.
1. The software _shall_ use a single Python file named _str_inspect.py_.
2. The software _shall_ read a sentence from the command line (e.g. python str_inspect.py "Please inspect this sentence thoroughly for the longest and shortest word.")
3. The software _shall_ output four lines of text matching this format:  
  >Shortest word: for    
  It is 3 characters
  Longest word: thoroughly    
  It is 10 characters
  
Notice that there are several words that are 3 characters in length and are "tied" for the shortest word.  Use the first one (in this case, "for") and ignore the others.  The same applies to the longest word if there are more than one with the same character count.  Also, if the shortest word is a single character ("a", or "I"), make sure the word "character" is not plural! For example:
  >Shortest word: a    
  It is 1 character
