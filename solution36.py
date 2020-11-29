#36.Write a Python program to sum all the items in a dictionary.
dict = {'d1': 10, 'd2': 20, 'd3': 30, 'd4': 40, 'd5': 50, 'd6': 60}
print(sum(dict.values()))


#37.Write a Python program to multiply all the items in a dictionary.
dict1 = {'d1': 1, 'd2': 2, 'd3': 3, 'd4': 4, 'd5': 5, 'd6': 6}
mul = 1
for x in dict1:
    mul *= dict1[x]
print(mul)
