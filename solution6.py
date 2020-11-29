#7Write a Python function that takes a list of words and returns the length of thelongest one.
def find_longest_one(word):
    word_len = []
    for n in word:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len

print(find_longest_one(['php','java','sandesh']))