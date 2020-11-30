#6.Write a Python program to find the first appearance of the substring 'not' and'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor'substring with 'good'. Return the resulting string.
def not_poor(str1):
    findnot = str1.find('not')
    findpoor = str1.find('poor')

    if findpoor > findnot and findnot > 0 and findpoor > 0:
        str1 = str1.replace(str1[findnot:(findpoor + 4)], 'good')
        return str1
    else:
        return str1


print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))
