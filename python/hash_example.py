
import os
import string

try:
    text = open('python/input.txt', 'r')
except IOError:
    print("can't open input file")
    os._exit(1)

common_words = ['the', 'and', 'a', 'to', 'be']

def get_words(file):
    for line in file:
        for word in line.lower().split():
            if word not in common_words:
                yield word.strip(string.punctuation + "")

freq_dict = {}

for word in get_words(text):
    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

print(freq_dict)