#45.Write a Python program to find the index of an item of a tuple1
tuple1 = ('a', 'b', 'c', 'd', 'e', 'a', 'c', 'd', 'a')
print(tuple1.index('d'))
#define the index from which you want to search
print(tuple1.index('c', 2))
#define the segement of the tuple1 to be searched.
print(tuple1.index('a', 6, 9))


#46.Write a Python program to find the length of a tuple
tup = tuple("InsightWorkshopAcademy")
print(tup)
print(len(tup))

