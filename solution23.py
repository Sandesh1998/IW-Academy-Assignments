#23.Write a Python program to check a list is empty or not.
list = []
if not list:
    print("empty list")

#24.Write a Python program to clone or copy a list.
list1 = [1, 2, 3, 4, 5]
newlist = list1
newlist.append(6)
print(list1)
print(newlist)