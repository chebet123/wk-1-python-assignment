# Basic Calculator Program

# Ask the user to enter the first number
num1 = float(input("Enter the first number: "))
#  Ask the user to enter the second number
num2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
operation = input("Enter an operation (+, -, *, /): ")

# Perform the calculation based on the user's choice
result = 0
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    # Check for division by zero
    if num2 != 0:
        result = num1 / num2
    else:
        print("❌Error: Cannot divide by zero!")
        exit()
else:
    print("❌Error: Invalid operation! Please use +, -, *, or /")
    exit()

# Print the result
print(f"{num1} {operation} {num2} = {result}")