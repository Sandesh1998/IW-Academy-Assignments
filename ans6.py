# 6.Write a Python function to check whether a number is in a given range.
def func_range(num):
    if num in range(2,7):
        print("%s is in the range" % str(num))
    else:
         print("The number is not in a range")
func_range(9)
