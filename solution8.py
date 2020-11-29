#8.Write a Python program to remove the nth index character from a non empty string.
def removeindex(str , n):
    return str[:n] + str[n+1:]

print(removeindex('python',0))
print(removeindex('javascript',5))
print(removeindex('sandesh',6))