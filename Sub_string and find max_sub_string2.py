"""Problem 3: Duplicated Substrings
read whole string from terminal"""
from string import *

s = input('Enter a string: ')
n = int(input('Enter a number: '))


def find_dup_string(s, n):
    found = 0
    list_word = '""'
    if n == 0:
        return list_word
    for index_one in range(0, len(s)):
        if found == 1:
            break
        current_word = s[index_one: n + index_one]      # slicing from current index_one to n length
        for index_two in range(index_one + 1, len(s) - 1):  # index_two starting from index_one + 1 to the len - 1
            word_to_compare = s[index_two: n + index_two]
            if current_word == word_to_compare:
                # would like to return instead of print out
                list_word = current_word
                found = 1
                # only return one result
    return list_word


def find_max_dup(s):
    #use find_dup_string
    list_word = ""
    for index in range(0, len(s)):
        find_max = find_dup_string(s, index)
        if find_max != '""':
            list_word = find_max
    return list_word


x = find_dup_string(s, n)
print(x)
y = find_max_dup(s)
print(y)

