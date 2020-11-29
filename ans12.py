# 12. Write a Python program to create a function that takes one argument, andthat argument will be multiplied with an unknown given number.
def func_unknown_mul(n):
    return lambda x: x * n
result = func_unknown_mul(2)
print(result(2))
print("Multiple 2 and 5 is :", result(5))
print("Multiple 2 and 7 is :", result(7))