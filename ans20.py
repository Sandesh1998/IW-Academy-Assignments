# 20.Write a Python program to find intersection of two given arrays usingLambda.
array1 = [1, 2, 3, 4, 5, 6, 7, 8]
array2 = [ 1, 3, 8, 5, 9]
print(array1)
print(array2)
intersection = list(filter(lambda x : x in array1 ,array2))
print("Intersection of given two arrays:" , intersection)