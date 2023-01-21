#find palindromes in the dictionary file

import load_dictionary
import os

path = os.getcwd()

print(path)

word_list = load_dictionary.load('dictionary.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)
        """the forward slice is compared to the reversed slice. if they are identical, append"""

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
"""* = splat operator. takes a list as input and expands it into positional arguments in the function call"""
