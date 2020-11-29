#22. Write a Python program to remove duplicates from a list.
x = [10,20,30,20,10,40,50,60,20]
duplicate = set()
already = []
for y in x:
    if y is not duplicate:
        already.append(y)
        duplicate.add(y)
print(duplicate)

