# 9.Write a Python function that takes a number as a parameter and check thenumber is prime or not.
import math;
def fun_test_prime(n):
    if (n == 1):
        return False
    elif (n == 2):
        return True
    else:
        for x in range(2,math.ceil(math.sqrt(n+1))):
            if n % x == 0:
                return False
        return True
print(fun_test_prime(11))

