#5.Create a tuple with your first name, last name, and age. Create a list,people, and append your tuple to it.
# Make more tuples with the corresponding information from your friends and append them to the list. Sort the list.
# When you learn about sort method, you can use the key parameter to sort by any field in the tuple, first name, last name,or age

lists = [('Ram', 'chhetri', 21), ('ahyam', 'poudel', 20)]
result = []

lists.append(('eva', "Khate sandesh", 325))
print(lists)
lists = sorted(lists, key=lambda tup: tup[1], reverse=True)
print(lists)


