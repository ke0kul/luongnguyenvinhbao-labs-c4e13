numbers = [1, 3, 5, 7, -100, -300, 500]

min_number = numbers[0]
for index, number in enumerate(numbers):
    if min_number > number:
        min_number = number

print(min_number)
