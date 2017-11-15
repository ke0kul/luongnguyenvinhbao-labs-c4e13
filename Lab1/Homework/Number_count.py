print("NUMBER COUNT")
print("*" * 15)

numbers = [-1, -5, -10, 3, 7, 9, -5, -10, 3, 9, 7, 25, 50]

input_number = int(input("Enter a number: "))
number_count = 0

if input_number not in numbers:
    print("Not found")
else:
    for i in numbers:
        if input_number == i:
            number_count += 1
    print("{0} appears {1} time(s) in list".format(input_number, number_count))
