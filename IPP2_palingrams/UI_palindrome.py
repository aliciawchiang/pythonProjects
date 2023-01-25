# original code alicia chiang
# user input and checks if its a palindrome with recursion

import sys

def palindrome_recursion(word):
    character_index = len(word) - 1
    #print (character_index)
    for i in range(character_index):
        #print (i)
        #print (character_index - i)
        #print (word[i])
        #print (word[character_index - i])

        if word[i] != word[character_index - i]:
            #print("\n{} is not a palindrome".format(word))
            return False
    return      
   

while True:
    print ("\nenter a word and see if it's a palindrome!\n")
    word = input("word: ")

    if palindrome_recursion(word) is False:
        print ("\n~~~{} is not a palindrome~~~\n".format(word))
    else:
        print("\n~~~{} is a palindrome!!!~~~\n".format(word))

    try_again = input("\npress enter to try again! else n to quit\n")
        
    if try_again.lower() == "n":
        break
    
input("press enter to exit")

