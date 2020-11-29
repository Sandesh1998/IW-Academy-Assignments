#20.Write a Python program to count the number of strings where the stringlength is 2
# or more and the first and last character are same from a given list ofstrings.
def match_the_string(str):
    count = 0
    for x in str:
        if len(x) >1 and  x[0] == x[-1]:
            count += 1
    return  count
print(match_the_string(['abc', 'xyz', 'aba', '1221']))