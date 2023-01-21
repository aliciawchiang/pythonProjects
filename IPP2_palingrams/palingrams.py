import load_dictionary

word_list = load_dictionary.load('dictionary.txt')

#find word-pair palingrams
def find_palingrams():
    palingram_list = []
    for word in word_list:
        end = len(word) #find the length of the word
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[]


