#9.Write a Python program to change a given string to a new string where the firstand last chars have been exchanged
def changestring(str):
    return str[-1:] + str[1:-1] + str[:1]

print(changestring('abcd'))
print(changestring('1234'))
