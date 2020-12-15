#18 . Find a package in the Python standard library for dealing with JSON.Import the library module and inspect the attributes of the module.Use the help function to learn more about how to use the module.
# Serialize a dictionary mapping 'name' to your name and'age' to your age, to a JSON string. Deserialize the JSON back into Python.
import json

# {key:value mapping}
a = {"name": "John",
     "age": 31
     }


b = json.dumps(a)
c= json.loads(b)

print(type(b))

print(type(c))
print(b)
print(c)