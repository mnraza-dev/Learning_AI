# Operators

# Arithmetic Operators - Math operations
# +, -, *, /, //, %, **

# Comparison Operators - Compare two values
# ==, !=, >, <, >=, <=

# Logical Operators - Combine multiple conditions
# and, or, not

# Assignment Operators - Assign a value to a variable
# =, +=, -=, *=, /=, %=, **=

# Identity Operators - Check if two values are the same [Object memory location]
# is, is not

# Membership Operators - Check if a value is in a sequence
# in, not in

# Bitwise Operators - Bitwise operations
# &, |, ^, ~, <<, >>    

# Operator Precedence - The order of operations
# PEMDAS - Parentheses, Exponents, Multiplication and Division (from left to right), Addition and Subtraction (from left to right)

a = 5
b = 10

# Arithmetic Operators
print(a + b) # Addition
print(a - b) # Subtraction
print(a * b) # Multiplication
print(a / b) # Division
print(a // b) # Floor Division
print(a % b) # Modulus
print(a ** b) # Exponentiation

# Comparison Operators
print(a == b) # Equal
print(a != b) # Not Equal
print(a > b) # Greater Than
print(a < b) # Less Than
print(a >= b) # Greater Than or Equal To
print(a <= b) # Less Than or Equal To

# Logical Operators
"""
and - all conditions must be True => True, False otherwise
or - at least one condition must be True => True, False otherwise
not - single operand is False => True, True => False
"""
age = 18
print(a>5 and b<15) # And
print(a<1 or b==20) # Or
print(not a==10) # Not

# Assignment Operators
x = 10
x += 5
print(x)

x = 10
x -= 5
print(x)

x = 10
x *= 5
print(x)

x = 10
x /= 5
print(x)

# Identity Operators
print(a is b) # Is
print(a is not b) # Is Not

# Membership Operators
print(a in [1,2,3,4,5]) # In
print(a not in [1,2,3,4,5]) # Not In

# Bitwise Operators
print(a & b) # Bitwise AND
print(a | b) # Bitwise OR
print(a ^ b) # Bitwise XOR
print(~a) # Bitwise NOT
print(a << b) # Bitwise Left Shift
print(a >> b) # Bitwise Right Shift







