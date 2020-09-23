
path = 'paragraph_1.txt' #user_input("What is the name of the file you want to consider? ")

with open(path, "r") as f:
    para_list = [x for x in f]

para = ' '.join(para_list)

word_list = para.split(' ')
word_count = len(word_list)

sentence_list = para.split('.')
sentence_list.remove(sentence_list[-1])
sentence_count = len(sentence_list) # for end '' after last sentence

letter_count = sum([len(word) for word in word_list]) / word_count

sentence_words = [sent.split(' ') for sent in sentence_list]

sentence_length = sum([len(el)-1 for el in sentence_words]) / sentence_count

#   * Approximate word count
#   * Approximate sentence count
#   * Approximate letter count (per word)
#   * Average sentence length (in words)

print(word_count)
print(sentence_count)
print(letter_count)
print(sentence_length)
