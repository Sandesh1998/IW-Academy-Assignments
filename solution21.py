#21.Write a Python program to get a list, sorted in increasing order by the lastelement in each tuple1 from a given list of non-empty tuples.
def last(n):
    return n[-1]
def sort_lastelement_tuple(tuple):
    return sorted(tuple, key=last)
print(sort_lastelement_tuple([(2,4),(5,3),(6,1)]))