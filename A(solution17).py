# 17.Write a program that serves as a basic calculator.It asks for two numbers,
# then it asks for an operator.Gracefully deal with input that doesn't cleanly convert to numbers. Deal with division by zero errors.

number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))
operation = input('''
Please type in the math operation you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division
''')

if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    try:
        print('{} / {} = '.format(number_1, number_2))

        print(number_1 / number_2)
        pass
    except ZeroDivisionError:
        print("Divide by 0 Error")



else:
    print('You have not typed a valid operator, please run the program again.')