#Create a simple calculator program that can add, subtract, multiply, and divide two integers


def calculator():
    print("Simple Calculator")
    print("Select a arithmetic operation: \n +\n -\n *\n /\n ")
    

    arithmetic_operation = input("Enter the choice: ")
    if arithmetic_operation not in [ '+' , '-' , '*' , '/']:
        print("Please enter a valid operaation")
        return

    try:
        num_1 = int(input("Enter the first integer: "))
        num_2 = int(input("Enter the second integer: "))
    except ValueError:
        print("Invalid input. Please enter integers only")
        return

    if arithmetic_operation == "+":
        result = num_1 + num_2
        operation = "+"
    elif arithmetic_operation == "-":
        result = num_1 - num_2
        operation = "-"
    elif arithmetic_operation == "*":
        result = num_1 * num_2
        operation = "*"
    elif arithmetic_operation == "/":
        if num_2 == 0:
            print("Error: Division by zero is not valid")
            return
        result = num_1 / num_2
        operation = "/"

    print(f"The result of {num_1} {operation} {num_2} is: {result}")

calculator()

    