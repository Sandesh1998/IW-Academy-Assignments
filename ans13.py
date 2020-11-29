# 13.Write a Python program to sort a list of tuples using Lambda.
cases = [('Nepal', 100), ('USA', 50), ('England', 70), ('china', 40)]
print(cases)
cases.sort(key=lambda x : x[1])
print(cases)