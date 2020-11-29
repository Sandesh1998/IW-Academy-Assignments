#32.Write a Python script to generate and print a dictionary that contains anumber (between 1 and n) in the form (x, x*x).
n = int(input("Input a number:"))
dict = {x:x*x for x in range(n)}
print(dict)


#33.Write a Python script to print a dictionary where the keys are numbersbetween 1 and 15 (both included) and the values are square of key5
dict1 = {y:y*y for y in range(1,16)}
print(dict1)