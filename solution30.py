#30.Write a Python script to check whether a given key already exists in adictionary.
dict = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def exist_in_dict(value):
    if value in dict:
        print(" a given key already exists in a dictionary")
    else:
        print(" a given key doesnot exist in a dictionary")
exist_in_dict(50)
exist_in_dict(60)


#31.Write a Python program to iterate over dictionaries using for loops.
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for item in d.items():
      print(item)