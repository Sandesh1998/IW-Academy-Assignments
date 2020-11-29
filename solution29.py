#29.Write a Python script to concatenate following dictionaries to create a newone.
dict1 = {1:10, 2:20}
dict2 = {3:30, 4:40}
dict3 = {5:50,6:60}
dict4 = {**dict1,**dict2,**dict3}
print(dict4)


