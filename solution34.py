#34.Write a Python script to merge two Python dictionaries.
dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict4 = {**dict1, **dict2}
print(dict4)