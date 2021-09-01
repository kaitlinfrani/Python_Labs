# -*- coding: utf-8 -*-
"""
Kaitlin Frani
CPSC 223P-01
Mon Mar 22, 2021
kaitlinfrani@fullerton.edu
"""

# Constant definition
ASCII_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ASCII_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DECIMAL_DIGITS = "0123456789"

# Function definitions below this line
#add doc strings to all functions

#return true if all are upper or lower
def is_alpha(str):
    """
  Return true if all characters in string are upper or lowercase.
    
    Parameters
    ----------
    str : string
        characters in string.

    Returns
    -------
    bool
        True if string is alphabetic
        False if string contains other things besides letters.

    """
    bool_value = True
    for letter in str:
        if letter not in ASCII_LOWERCASE and letter not in ASCII_UPPERCASE:
            bool_value = False
    if bool_value == True:
        return True
    else:
        return False
    
#return true if all are decimals
def is_digit(str):
    """
   Return true if all are decimals

    Parameters
    ----------
    str : string
        will be used to check.

    Returns
    -------
    bool
        True if string are numbers
        False if string contains something else besides numbers.

    """
    bool_value = True
    for number in str:
        if number not in DECIMAL_DIGITS:
            bool_value = False
    if bool_value == True:
        return True
    else:
        return False

#return -1 if 2nd parameter is not length 1, 2nd parameter must be of length 1
def find_chr(str1, str2):
    """
   Will return lowest index where str2 is found within str1

    Parameters
    ----------
    str1 : string
        word 1 where str2 will be found within it
    str2 : string
        need to be of length 1

    Returns
    -------
    lowest index, i
        if str2 is of length 1, lowest index will be returned

    """
    if len(str2) != 1:
        return -1
    else:
        #need an index for each item to be referenced
        for i, characters in enumerate(str1):
            if characters == str2:
                return i
    return -1

#return string of the parameter where all upper turns to lower
#use the enumeration to get index, find_chr
def to_lower(str):
    """
    turns string from upper to lowercase

    Parameters
    ----------
    str : string
        will be used to convert to lower.

    Returns
    -------
    result : string
        uppercase string outputted.

    """
    result = ''
    for letters in str:
        if letters in ASCII_UPPERCASE:
            index = find_chr(ASCII_UPPERCASE, letters)
            result += ASCII_LOWERCASE[index]
        else:
            result += letters
    return result

#return string of parameter where all lower have been converted to upper
#same as to_lower but need to switch upper and lower
def to_upper(str):
    """
    turns string from lower to uppercase

    Parameters
    ----------
    str : string
        will be used to convert to uppercase.

    Returns
    -------
    result : string
        string is now in uppercase.

    """
    result = ''
    for letters in str:
        if letters in ASCII_LOWERCASE:
            index = find_chr(ASCII_LOWERCASE, letters)
            result += ASCII_UPPERCASE[index]
        else:
            result += letters
    return result
    
#return the lowest index where the second parameter is found within the first parameter
def find_str(str1, str2):
    """
    lowest index where str2 is found within str1

    Parameters
    ----------
    str1 : string
        for str2 to be within it.
    str2 : string
        must be length 1, going to check with str1.

    Returns
    -------
    lowest index, i
        if str2 is of length 1 and in str1, else it will return -1.

    """
    if str2 not in str1:
        return -1
    else:
        for i, letters in enumerate(str1):
            if letters == str2[0]:
                #copy list
                if str1[i:i + len(str2)] == str2:
                    return i

#2nd and 3rd parameters must be of length 1, returns the string which is a copy of the 
#first parameter
def replace_chr(str1, str2, str3):
    """
    str2 gets replaced by str3

    Parameters
    ----------
    str1 : string
        used for str2, str3 copy.
    str2 : string
        must be of length 1, will be replaced by str3.
    str3 : string
        must be of length 1, replaces str2.

    Returns
    -------
    string
        copy of str1 in str2 once str2 gets replaced by str3.

    """
    result = ""
    if len(str2) != 1 or len(str3) != 1:
        return -1
    elif str2 not in str1:
        return -1
    #if length is 1
    else:
        for i, letters in enumerate(str1):
            if letters == str2:
                result = result + str3
            else:
                result = result + letters
        #return copy of first parameter
        return result

#returns the string which is a copy of the first parameter
def replace_str(str1, str2, str3):
    """
    returns copy of str1 if str2 gets replaced by str3

    Parameters
    ----------
    str1 : string
        copy will be returned based on str2.
    str2 : string
        must be of length 1, if in str1, will return str1 and str3 copy.
    str3 : string
        will be returned in the copy.

    Returns
    -------
    string
        copy of first parameter.

    """
    result = ""
    if str2 not in str1:
        return str1
    elif str2 == "":
        return str3 + str1 + str3
    
    else:
        for i, ch in enumerate(str1):
            if ch == str2[0]:
                if str1[i:i + len(str2)] == str2:
                    result = str1[:i] + str3 + str1[i + len(str2):]
        return result