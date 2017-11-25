from random import *

while True:
    x = randrange(0, 100)
    y = randrange(0, 100)
    error = randrange(-2, 2)
    ops = ['+', '-', '*', '/']
    op = choice(ops)

    if op == '+':
        result = x + y + error
    elif op == '-':
        result = x - y + error
    elif op == '*':
        result = x * y + error
    else:
        if y == 0:
            y = randrange(1, 100)
        result = x / y + error
    print(x, op, y, "=", result)

    user_choice = input("Y/N?")

    if error == 0:
        if user_choice == "Y" or user_choice == "y":
            print("Yay")
        else:
            print("Oops")
    else:
        if user_choice == "N" or user_choice == "n":
            print("Yay")
        else:
            print("Oops")
