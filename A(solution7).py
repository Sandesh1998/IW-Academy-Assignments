# 7 .Create a list of tuples of first name,lastname, and age for your friends and colleagues.If you don't know the age ,put in None.Calculate the averageage,
# skipping over any None values.Print out each name,followed by old or young if they are above or below the average age


def printName(name, type):
    print(name + ":" + type)


lists=[('Ram', 'chhetri', 21), ('ahyam', 'poudel', 20), ('ahyam', 'poudel', None)]
result_list=list(filter(lambda x: x[2] is not None, lists))
average=sum([a[2] for a in result_list]) / len(result_list)

[printName(a[0], "old") if a[2] > average else printName(a[0], "young") for a in result_list]
