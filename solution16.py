#16.Write a Python program to sum all the items in a list
def list_sum(item):
    sum = 0
    for i in item:
        sum += i
    return  sum
print(list_sum([1,2,3,4,5]))


#17.Write a Python program to multiplies all the items in a list.
def list_mul(item):
    mul = 1
    for j in item:
        mul *=j
    return mul

print(list_mul([1,2,3]))
