#38.Write a Python program to remove a key from a dictionary.
dict = {'d1': 10, 'd2': 20, 'd3': 30, 'd4': 40, 'd5': 50, 'd6': 60}
print(dict)
if 'd1' in dict:
    del dict['d1']
print(dict)