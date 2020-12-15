def generate_decorated(func):
    def inner(*args, **kwargs):
        print("dynamic arguments")
        return func(*args, **kwargs)
    return inner


def add(a, b, c):
    return a+b+c
add = generate_decorated(add)
print(add(2,4,6))