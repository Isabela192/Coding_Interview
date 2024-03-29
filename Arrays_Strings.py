# 1.1 Is Unique:
# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def is_unique(string):
    # Assuming ASCII characters (total 128)
    if len(string) > 128:
        return False

    char_set = [False] * 128
    for char in string:
        if char_set[ord(char)]:
            return False
        char_set[ord(char)] = True

    return True


test_string = "abcdefghijklmnopqrstuvwxyz"
print(is_unique(test_string))


# 1.2 Check Permutation:
# Given two strings, write a method to decide if one is a permutation of the other.

def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False

    char_count = [0] * 128

    for char in str1:
        char_count[ord(char)] += 1

    for char in str2:
        char_count[ord(char)] -= 1
        if char_count[ord(char)] < 0:
            return False

    return True

string_a = "abcdefghijklmnopqrstuvwxyz"
string_b = "znopqrstuvwxyabcdefghijklm"
print(is_permutation(string_a, string_b))


# 1.3 URLify:
# Write a method to replace all spaces in a string with '%20'
# You may assume that the string has sufficient space at the end to hold the additional characters, and thtat you are given the "true" length of the string.


def URLify(s):

    return s.replace(" ", "%20")


s = "Mr John Smith    "
print(URLify(s))


# 1.4 Palindrome Permutation:
# Given a string, write a function to check if it is a permutation of a palindrome.

def is_palindrome_permutation(string):

    string = string.replace(" ", "")
    string = string.lower()

    if string == string[::-1]:
        return True

    else:
        return False


string_test = "Taco Cat"
print(is_palindrome_permutation(string_test))


# 1.5 One Away:
# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
def one_edit_away(a, b):
    i = 0
    while i <= len(a):
        for i in range(0, len(a)):
            if a[i] != b[i]:
                return False
            else:
                return True


def one_insert_away(a, b):
    i = 0
    j = 0
    while (i <= len(a)) and (j <= len(b)):
        if a[i] != b[j]:
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1

    return True


def one_away(a, b):
    if len(a) == len(b):
        return one_edit_away(a, b)

    if len(a)-1 == len(b):
        return one_insert_away(a, b)

    if len(a)+1 == len(b):
        print("len(a)+1 == len(b)")
        return one_insert_away(a, b)


print(one_away("pale", "ple"))
print(one_away("pale", "bake"))


# 1.6 String Compression:
# Implement a method to perform basic string compression using the counts of repeated characters.

def string_compression(s):
    compressed_string = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed_string += s[i-1] + str(count)
            count = 1

    compressed_string += s[-1] + str(count)

    if len(compressed_string) < len(s):
        return compressed_string
    else:
        return s


print(string_compression("aabcccccaaa"))
print(string_compression("abcdef"))


# 1.7 Rotate Matrix:
# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees. Can you do this in place?
def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n//2):
        first = layer
        last = n-1-layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[i][last]
            matrix[i][last] = top
    return matrix


print(rotate_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


# 1.8 Zero Matrix:
# Write an algorithm such that if an element in a MxN matrix is 0, 
# it's entire row and column are et to 0
def zero_matrix(matrix):
    row = []
    col = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                if i not in row:
                    row.append(i)
                if j not in col:
                    col.append(j)
                    
    for row_index in row:
        for index in range(len(matrix[0])):
            matrix[row_index][index] = 0
            
    for col_index in col:
        for index in range(len(matrix)):
            matrix[index][col_index] = 0
            
    return matrix
            
print(zero_matrix([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))

#1.9 String Rotation: Assume you have a method isSubstring which checks if one
# word is a substring of another. Given two strings s1 and s2, write code to 
# check if s2 is a rotation of s1 using only one call to isSubstring 

def is_substring(s1: str, s2: str):
    return len(s1) == len(s2) and s2 in s1*2

print(is_substring("waterbottle", "erbottlewat"))
