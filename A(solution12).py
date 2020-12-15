# 12. Create a function, is_palindrome, to determine if a supplied word isthe same if the letters are reversed.
def isPalindrome(string):
    lp = 0
    rp = len(string) - 1

    while rp >= lp:
        if not string[lp] == string[rp]:
            return False
        lp += 1
        rp -= 1
    return True


print(isPalindrome(input("Enter a string:")))