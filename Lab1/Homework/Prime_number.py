print("PRIME NUMBER CHECK")
print("*" * 20)

input_number = int(input("Enter a number: "))

if input_number < 0:
    print("Error, Input number can't < 0")
elif input_number == 0 or input_number == 1:
    print(input_number, " is not a prime number")
else:
    count = 0
    for i in range (2, input_number):
        if input_number % i == 0:
            count += 1
        else:
            pass
    if count == 0:
        print(input_number, " is a prime number")
    else:
        print(input_number, " is not a prime number")
