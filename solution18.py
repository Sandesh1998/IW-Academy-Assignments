#18.Write a Python program to get the largest number from a list.
def largest_in_list(items):
    max =items[0]
    for i in items:
        if i > max:
            max = i
    return max
print(largest_in_list([1,2,-4,5,3,8]))

#19.Write a Python program to get the smallest number from a list.
def smallest_in_list(items):
    min = 0
    for i in items:
        if i < min:
            min = i
    return min
print(smallest_in_list([0,1,2,4,5,3,-5]))