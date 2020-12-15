# 6.Create a list with the names of friends and colleagues. Search for thename ‘John’ using a for a loop.
# Print ‘not found’ if you didn't find it.
friend_list = ['sandesh', 'joe', 'Kushal', 'Binod']
#take the friend name that you want to search
friend_name = input("Enter a friend name:")
if friend_name.lower() in friend_list:
    print("%s is found in list"%(friend_name))
else:
    print("%s is not found in list" % (friend_name))
