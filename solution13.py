#13.Write a Python program that accepts a comma separated sequence of wordsas input and prints the unique words in sorted form (alphanumerically).
words = input("Input a sequence of a word sepaerated by comma:")
items = [item for item in words.split(",")]
print(",".join(sorted(list(items))))
