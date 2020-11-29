def fun_reverse(str):
    str1 = ''
    index = len(str)
    while index > 0:
        str1 += str[index -1]
        index = index -1
    return str1
print(fun_reverse("1234abcd"))
