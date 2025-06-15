start = int(input("Enter the start of the range: "))
stop = int(input("Enter the stop of the range: "))

skip = int(input("Enter the skip number: "))

for i in range(start, stop, skip):
    if i % skip == 0:
        print(f"Divisible by {skip}: {i}")
    else:
        print(f"Not divisible by {skip}: {i}")





