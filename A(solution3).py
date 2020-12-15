sentence = [" The taste of liquid state of the cream is bad then in ice form.And the act of the cat is hilarious."]
list = (sentence[0]. split())
anagram_list = []
for word1 in list:
    for word2 in list:
        if word1 != word2 and (sorted(word1.lower()) == sorted(word2.lower())):
            anagram_list.append(word1.lower())
print(anagram_list)