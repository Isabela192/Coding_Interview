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
print(urlify(string))
