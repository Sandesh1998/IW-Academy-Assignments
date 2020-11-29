#2.Write a Python function to sum all the numbers in a list.
def fun_sum(item):
    sum = 0
    for i in item:
        sum += i
    return  sum
print(fun_sum((8, 2, 3, 0, 7)))

#3.Write a Python function to multiply all the numbers in a list.
def fun_mult(num):
    mul = 1
    for j in num:
        mul *= j
    return mul
print(fun_mult((8, 2, 3, -1, 7)))