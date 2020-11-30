# 10. Write a Python program to print the even numbers from a given list
def func_even(item):
    list = []
    for x in item:
        if x % 2 == 0:
            list .append(x)
    return list
print(func_even([1,2,3,4,5,6,7,8,9]))