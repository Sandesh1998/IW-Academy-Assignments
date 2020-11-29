#1.Write a Python function to find the Max of three numbers.
def max(x,y,z):
    if (x >= y) and (x >= z):
        largest = x
    if (y >= x) and (y >= z):
        largest = y
    else:
        largest = z
        return largest
print(max(1,3,4))

def max_two(x,y):
    if x > y:
        return x
    return y
def max_three(x,y,z):
    return max_two(x, max_two(y, z))
print(max_three(1,2,15))
