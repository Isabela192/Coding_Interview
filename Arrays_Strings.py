# 1.1 Is Unique:
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

from collections import Counter


def isUnique(string):

    if len(string) == len(Counter(string)):
        return True

    else:
        return False


test_string = "abcdefghijklmnopqrstuvwxyz"
print(isUnique(test_string))


# 1.2 Check Permutation:
# Given two strings, write a method to decide if one is a permutation of the other.


def isPermutation(string_a, string_b):

    if len(string_a) != len(string_b):
        return False

    return Counter(string_a) == Counter(string_b)


string_a = "abcdefghijklmnopqrstuvwxyz"
string_b = "zyxwvutsrqponmlkjihgfe1cba"
print(isPermutation(string_a, string_b))


# 1.3 URLify:
# Write a method to replace all spaces in a string with '%20'
# You may assume that the string has sufficient space at the end to hold the additional characters, and thtat you are given the "true" length of the string.


def URLify(string):

    return string.replace(" ", "%20")


string = "Mr John Smith    "
print(URLify(string))


# 1.4 Palindrome Permutation:
# Given a string, write a function to check if it is a permutation of a palindrome.

def isPalindromePermutation(string):

    string = string.replace(" ", "")
    string = string.lower()

    if string == string[::-1]:
        return True

    else:
        return False
    
string_test = "Taco Cat"
print(isPalindromePermutation(string_test))    


# 1.5 One Away:
# There are three types of edits that can be performed on strings: insert a character, 
# remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
def oneEditReplace(string_a, string_b):

    count = 0

    for i in range(len(string_a)):
        if string_a[i] != string_b[i]:
            count += 1

        if count > 1:
            return False

    return True
  
    

def oneAway(string_a, string_b):

    if len(string_a) == len(string_b):
        return oneEditReplace(string_a, string_b)

    elif len(string_a) + 1 == len(string_b):
        return oneEditInsert(string_a, string_b)

    elif len(string_a) - 1 == len(string_b):
        return oneEditInsert(string_b, string_a)

    else:
        return False

print(oneAway("pale", "ple"))