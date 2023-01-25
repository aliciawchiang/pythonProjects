# alicia chiang original code off of book psuedocode
# jan 25
import load_dictionary

# load digital dictionary file as a list of words
word_list = load_dictionary.load('dictionary.txt')

# accept word from user
print ("\nenter a word to find anagrams!\n")
userWord = input("word: ")

# sort the user word
sortedUserWord = sorted(userWord)

def find_anagrams():
    anagram_list = []
    words = set(word_list)
    for word in words: # loop through the dictionary file
        sorted_word = sorted(word) # sort each dictionary word
        if sorted_word == sortedUserWord:
            anagram_list.append(word)
    return anagram_list

anagrams = find_anagrams()

print("\nNumber of anagrams = {}\n".format(len(anagrams)))

for i in anagrams:
    print("{}".format(i))

