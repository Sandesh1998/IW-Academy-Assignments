# 8.Write a Python function that takes a list and returns a new list with unique elements of the first list
def fun_unique_list(N):
    l = []
    for x in N:
        if x not in l:
            l.append(x)
    return l


print(fun_unique_list([1,2,3,3,3,3,4,5]))
