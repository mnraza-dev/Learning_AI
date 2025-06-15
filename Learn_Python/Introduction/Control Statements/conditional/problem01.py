age = int(input("Enter your age: "))

if age >= 18 and age <100:
    print("You can cast your vote")
elif age <=0 or age >100:
    print("Invalid age")
elif age >= 16 and age <18:
    print("You can't cast your vote but you can vote in the next election")
else:
    print("Error occurred !")