# 9 . Write a binary search function.It should take a sorted sequence and the item it is looking for.
# It should return the index of the item if found.It should return -1 if the item is not found
def binary_search_recursive(array, element, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2
    if element == array[mid]:
        return mid

    if element < array[mid]:
        return binary_search_recursive(array, element, start, mid-1)
    else:
        return binary_search_recursive(array, element, mid+1, end)
element = 29

array = [1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29]

print("Searching for {} in {}".format(element, array,0, 30))
print("Index of {}: {}".format(element, binary_search_recursive(array, element,0,10)))