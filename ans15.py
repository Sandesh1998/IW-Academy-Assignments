# 15.Write a Python program to filter a list of integers using Lambda.
item = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(item)
even = list(filter(lambda x: x % 2 == 0 ,item))
print("Even numbers:", even)



