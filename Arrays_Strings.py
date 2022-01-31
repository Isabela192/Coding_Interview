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
test_string_repeat = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
print(isUnique(test_string))
print(isUnique(test_string_repeat))