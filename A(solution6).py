#6.Create a list with the names of friends and colleagues.
# Search for thename ‘John’ using a for a loop. Print ‘not found’ if you didn't find it.
def isNameExist(list, name):
    for word in list:
        if word == name:
            return "John is found"
    return "Not found"


list_ed = ['ram', 'eva', 'John', 'shyam']
print(isNameExist(list_ed, 'John'))
