#43.Write a Python program to remove an item from a tuple1.
tup = ('p', 'y', 't', 'h', 'o', 'n')
print(tup)
#As we know tuple1 is immutable,so we cannot remove it.
#So now we first change tuple1 into list and remove it.
list = list(tup)
list.remove('p')
#After removing item  from list again we will change list into tuple1.
tup = tuple(list)
print(tup)