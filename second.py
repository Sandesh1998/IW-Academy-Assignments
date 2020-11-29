
def change_char(str1):
    return str1[0] + str1[1:].replace(str1[0], '$')
   
print(change_char('restart'))

