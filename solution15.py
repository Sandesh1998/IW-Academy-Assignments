def insert_middle_string(str , word):
    return str[:2] + word + str[2:]
print(insert_middle_string('[[]]','python'))
print(insert_middle_string('{{}}','php'))