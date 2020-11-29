# 16.Write a Python program to square and cube every number in a given list ofintegers using Lambda.
num = [1, 2, 3, 4, 5, 6]
print(num)
square = list(map(lambda x: x**2 , num))
print("Square:",square)
CUBE = list(map(lambda x: x**3 , num))
print("Cube:",CUBE)
