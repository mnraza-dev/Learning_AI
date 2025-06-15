num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))

choice = input("Enter the choice: +, -, *, /, %, **, //: ")
if choice == "+":
    print(f"The sum of {num_1} and {num_2} is {num_1 + num_2}")
elif choice == "-":
    print(f"The difference of {num_1} and {num_2} is {num_1 - num_2}")
elif choice == "*":
    print(f"The product of {num_1} and {num_2} is {num_1 * num_2}")
elif choice == "/":
    print(f"The quotient of {num_1} and {num_2} is {num_1 / num_2}")
elif choice == "%":
    print(f"The remainder of {num_1} and {num_2} is {num_1 % num_2}")
elif choice == "**":
    print(f"The power of {num_1} and {num_2} is {num_1 ** num_2}")
elif choice == "//":
    print(f"The floor division of {num_1} and {num_2} is {num_1 // num_2}")
else:
    print("Invalid choice")