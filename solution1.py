# 1.Write a Python program to count the number of characters (characterfrequency) in a string.
def calculateCharacter(strInput):
    character = {}
    for i in strInput:
        if i in character:
            character[i] += 1
        else:
            character[i] = 1
    return character

print(calculateCharacter("Google is good"))

