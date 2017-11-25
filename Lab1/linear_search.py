numbers = [-5, 10, 55, -100, 8]

x = int(input("Enter a number: "))

found_index = -1

for index, number in enumerate(numbers):
    if x == number:
        found_index = index
        break
if found_index == -1:
    print("Not found")
else:
    print("Found: ", found_index)
