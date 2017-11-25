numbers = [1, 2, 3, 45, 55, 66, 79, 813, 932, 1053, 9999]
x = int(input("Enter a number: "))
start = 0
stop = len(numbers)
found_index = -1

while start != stop:
    mid = (start + stop) // 2
    if numbers[mid] == x:
        found_index = mid
        break
    elif numbers[mid] > x:
        stop = mid
    else:
        start = mid

if found_index == -1:
    print("Not found")
else:
    print("found at: ", found_index)
