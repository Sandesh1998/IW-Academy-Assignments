# 18.Write a Python program to check whether a given string is number or notusing Lambda.
num = lambda s: s.replace('.', '', 1).isdigit()
print(num('1234'))
print(num('00000'))
print(num('1.2345'))
print(num('-12345'))
print(num('F001'))
print("Lets check a  negative numbers")
num1 = lambda r: num(r[1:]) if r[0] == '-' else num(r)
print(num1('-16.4'))
print(num1('-24587.11'))