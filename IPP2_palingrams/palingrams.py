# list runtime was 50.432s
# set runtume is 0.111s
import load_dictionary

word_list = load_dictionary.load('dictionary.txt')

#find word-pair palingrams
def find_palingrams():
    palingram_list = []
    words = set(word_list) #creating a set of the word_list
    for word in words:
        end = len(word) #find the length of the word
        rev_word = word[::-1] #reverse the word
        if end > 1: #length of word over 1
            for i in range(end): 
                if word[i:] == rev_word[:end-i] and rev_word[end-i:] in words:
                    palingram_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:] and rev_word[:end-i] in words:
                    palingram_list.append((rev_word[:end-i], word))
    return palingram_list

palingrams = find_palingrams()
# sort palingrams on first word
palingrams_sorted = sorted(palingrams)

# display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))


