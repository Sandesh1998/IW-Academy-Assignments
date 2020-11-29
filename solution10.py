#10.Write a Python program to remove the characters which have odd indexvalues of a given string.
def remove_odd_index(str):
    return str[::2]
print(remove_odd_index(input('Enter Input:')))
