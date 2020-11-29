#5. Write a Python function to calculate the factorial of a number (a non-negativeinteger). The function accepts the number as an argument.5
def fun_fact(n):
    if n == 0:
        return 1
    else:
        return n * fun_fact(n-1)
n =int(input("Enter a number:"))
print(fun_fact(n))

