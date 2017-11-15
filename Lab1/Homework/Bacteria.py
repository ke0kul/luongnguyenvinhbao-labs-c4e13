bacteria_number = int(input("How much B barteria are there? "))
times = int(input("How much time in minutes will we wait? "))

for i in range (0, times, 2):
    bacteria_number += bacteria_number
print("After {0} minute(s), we would have {1} bacterias".format(times, bacteria_number))
