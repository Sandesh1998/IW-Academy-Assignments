#25. Write a Python program to check whether all dictionaries in a list are empty ornot.
list1 = [{},{},{}]
list2 = [{1,2},{},{}]
print(all(not d for d in list1))
print(all(not d for d in list2))






#26. Write a Python program to insert a given string at the beginning of all items ina list.
number = [1,2,3,4]
print(['emp{0}'.format(i) for i in number])