# 7.Write a Python function that accepts a string and calculate the number ofupper case letters and lower case letters.
def cal_ucase_lcase(str):
    l ={ "uppercase": 0, "lowercase": 0}
    for x in str:
       if x.isupper():
        l["uppercase"] += 1
       elif x.islower():
        l["lowercase"] += 1
    else:

        print("Original string:", str)
        print("The  length of uppercase is:", l["uppercase"])
        print("The length of lower case is:", l["lowercase"])
cal_ucase_lcase("The quick Brow Fox")