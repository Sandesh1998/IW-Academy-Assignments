# 14.Write a Python program to sort a list of dictionaries using Lambda.
student = [{'Name': 'Ram', 'Roll':16, 'Address': 'Pokhara'}, {'Name': 'sita', 'Roll': '2', 'Address': 'KTM'}, {'Name': 'Joe', 'Roll': 7, 'Address': 'Chitwan'}]
print(student)
sorted_models = sorted(student, key = lambda x: x['Address'])
print(sorted_models)
