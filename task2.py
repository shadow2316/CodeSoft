def simple_calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Take input from the user for operation
    operation = int(input("Enter choice (1/2/3/4): "))

    # Take input from the user for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the chosen operation and display the result
    if operation == 1:
        print("Result:", num1 + num2)
    elif operation == 2:
        print("Result:", num1 - num2)
    elif operation == 3:
        print("Result:", num1 * num2)
    elif operation == 4:
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice.")

simple_calculator()

