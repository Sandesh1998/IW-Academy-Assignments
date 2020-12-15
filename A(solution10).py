# 10 . Write a function that takes camel-cased strings(i.e.This Is Camel Cased),and converts them to snake case(i.e.this_is_camel_cased).
# Modify the function by adding an argument,separator,so it will also convert to the kebab case(i.e.this-is-camel-case) as well.
from functools import reduce


def change_case(str, sep):
    return reduce(lambda x, y: x + (sep if y.isupper() else '') + y, str).lower()


# Driver code
str = "GeeksForGeeks"
print(change_case(str, "_"))
