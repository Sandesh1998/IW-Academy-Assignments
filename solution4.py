def mergeString(str1, str2):
    return str2[:2] + str1[2:] + " " + str1[:2] + str2[2:]
print(mergeString(input("str1:"), input("str2:")))
