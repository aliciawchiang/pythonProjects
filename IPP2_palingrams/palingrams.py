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
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in word_list:
                    palingram_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in word_list:
                    palingram_list.append((rev_word[:end-i], word))
    return palingram_list

palingrams = find_palingrams()
# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))


