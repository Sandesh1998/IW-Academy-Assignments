# 4. Create a list. Append the names of your colleagues and friends to it.
# Has the id of the list changed? Sort the list. What is the first item on
# the list? What is the second item on the list?
Name = ['ram', 'shyam', 'mac', 'sandy', 'eva']
for n in range(len(Name)):
  print(f"{id(Name[n])} {n+1}th item is :{Name[n]}")
print("-----------------------------------------------")
Add_Name = ['rit', 'jhi', 'gun', 'buddy']
for name in Add_Name:
  Name == Name.append(name)
Name==Name.sort()
for n in range(len(Name)):
  print(f"{id(Name[n])} {n+1}th item is :{Name[n]}")
''' NO the id of wasn't changed. First item on list is "buddy" and second item on list is "eva". '''