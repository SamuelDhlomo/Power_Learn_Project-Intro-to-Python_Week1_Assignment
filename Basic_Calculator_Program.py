def calculator():
    # Ask the user for the first number
    num1 = float(input("Enter the first number: "))

    # Ask the user for the operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Ask the user for the second number
    num2 = float(input("Enter the second number: "))

    # Perform the operation based on the user's input
    if operation == "+":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "/":
        # Check for division by zero
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Error: Invalid operation. Please try again.")

