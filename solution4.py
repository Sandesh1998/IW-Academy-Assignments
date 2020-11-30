# 4.Write a Python program to get a single string from two given strings, separatedby a space and swap the first two characters of each string.
def mergeString(str1, str2):
    return str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]
print(mergeString(input("str1:"), input("str2:")))
