"""
Write a program to print the sum of the given range of numbers
"""
sum = 0
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for i in range(start, end):
    sum += i #sum = sum + i
print(f"The sum of the given range of numbers is {sum}")


