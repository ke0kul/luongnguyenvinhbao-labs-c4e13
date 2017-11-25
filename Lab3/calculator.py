def eval(x, y, op):
    if op == '+':
        result = x + y
    elif op == '-':
        result = x - y
    elif op == '*':
        result = x * y
    elif op == '/':
        if y == 0:
            print("NaN")
        else:
            result = x / y
    return result

# x = int(input("Enter x:"))
# op = input("Choose an operation (+, - , *, /):")
# y = int(input("Enter y:"))
# if op in ['+', '-', '*', '/']:
#     r = eval()
#     print(r)
# else:
#     print("Invalid input")
#     break
