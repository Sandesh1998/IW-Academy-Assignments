# 3.Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def change_char(str1):
    return str1[0] + str1[1:].replace(str1[0], '$')
   
print(change_char('restart'))

